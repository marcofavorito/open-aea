# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2022 Valory AG
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This test module contains AEA cli tests for Libp2p tcp client connection."""
import json
import os

from aea.helpers.base import CertRequest
from aea.multiplexer import Multiplexer
from aea.test_tools.test_cases import AEATestCaseEmpty

from packages.valory.connections import p2p_libp2p_client
from packages.valory.connections.p2p_libp2p_client.connection import PUBLIC_ID

from tests.conftest import DEFAULT_LEDGER, _make_libp2p_connection
from tests.conftest import default_ports as ports
from tests.conftest import libp2p_log_on_failure, libp2p_log_on_failure_all


p2p_libp2p_client_path = f"vendor.{p2p_libp2p_client.__name__.split('.', 1)[-1]}"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_CLIENTS_PER_NODE = 4

DEFAULT_LAUNCH_TIMEOUT = 10


@libp2p_log_on_failure_all
class TestP2PLibp2pClientConnectionAEARunning(AEATestCaseEmpty):
    """Test AEA with p2p_libp2p_client connection is correctly run"""

    @classmethod
    @libp2p_log_on_failure
    def setup_class(cls):
        """Set up the test class."""
        super().setup_class()

        temp_dir = os.path.join(cls.t, "temp_dir_node")
        os.mkdir(temp_dir)
        cls.delegate_port = next(ports)
        cls.node_connection = _make_libp2p_connection(
            data_dir=temp_dir,
            delegate_host=DEFAULT_HOST,
            delegate_port=cls.delegate_port,
            delegate=True,
        )
        cls.node_multiplexer = Multiplexer([cls.node_connection])
        cls.log_files = [cls.node_connection.node.log_file]

        cls.node_multiplexer.connect()

    def test_node(self):
        """Test the node is connected."""
        assert self.node_connection.is_connected is True

    def test_connection(self):
        """Test the connection can be used in an aea."""
        ledger_id = DEFAULT_LEDGER
        self.generate_private_key(ledger_id)
        self.add_private_key(ledger_id, f"{ledger_id}_private_key.txt")
        self.set_config("agent.default_ledger", ledger_id)
        self.set_config("agent.required_ledgers", json.dumps([ledger_id]), "list")
        self.add_item("connection", str(PUBLIC_ID))
        conn_path = p2p_libp2p_client_path
        self.nested_set_config(
            conn_path + ".config",
            {
                "nodes": [
                    {
                        "uri": "{}:{}".format(DEFAULT_HOST, self.delegate_port),
                        "public_key": self.node_connection.node.pub,
                    }
                ]
            },
        )

        # generate certificates for connection
        self.nested_set_config(
            conn_path + ".cert_requests",
            [
                CertRequest(
                    identifier="acn",
                    ledger_id=ledger_id,
                    not_after="2022-01-01",
                    not_before="2021-01-01",
                    public_key=self.node_connection.node.pub,
                    message_format="{public_key}",
                    save_path="./cli_test_cert.txt",
                )
            ],
        )
        self.run_cli_command("issue-certificates", cwd=self._get_cwd())

        process = self.run_agent()
        is_running = self.is_running(process, timeout=DEFAULT_LAUNCH_TIMEOUT)
        assert is_running, "AEA not running within timeout!"

        check_strings = "Successfully connected to libp2p node {}:{}".format(
            DEFAULT_HOST, self.delegate_port
        )
        missing_strings = self.missing_from_output(process, check_strings)
        assert (
            missing_strings == []
        ), "Strings {} didn't appear in agent output.".format(missing_strings)

        self.terminate_agents(process)
        assert self.is_successfully_terminated(
            process
        ), "AEA wasn't successfully terminated."

    @classmethod
    def teardown_class(cls):
        """Tear down the test"""
        cls.terminate_agents()
        super().teardown_class()
        cls.node_multiplexer.disconnect()
