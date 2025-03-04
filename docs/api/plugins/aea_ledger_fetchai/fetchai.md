<a id="plugins.aea-ledger-fetchai.aea_ledger_fetchai.fetchai"></a>

# plugins.aea-ledger-fetchai.aea`_`ledger`_`fetchai.fetchai

Fetchai module wrapping the public and private key cryptography and ledger api.

<a id="plugins.aea-ledger-fetchai.aea_ledger_fetchai.fetchai.FetchAIHelper"></a>

## FetchAIHelper Objects

```python
class FetchAIHelper(CosmosHelper)
```

Helper class usable as Mixin for FetchAIApi or as standalone class.

<a id="plugins.aea-ledger-fetchai.aea_ledger_fetchai.fetchai.FetchAICrypto"></a>

## FetchAICrypto Objects

```python
class FetchAICrypto(CosmosCrypto)
```

Class wrapping the Entity Generation from Fetch.AI ledger.

<a id="plugins.aea-ledger-fetchai.aea_ledger_fetchai.fetchai.FetchAIApi"></a>

## FetchAIApi Objects

```python
class FetchAIApi(_CosmosApi, FetchAIHelper)
```

Class to interact with the Fetch ledger APIs.

<a id="plugins.aea-ledger-fetchai.aea_ledger_fetchai.fetchai.FetchAIApi.__init__"></a>

#### `__`init`__`

```python
def __init__(**kwargs: Any) -> None
```

Initialize the Fetch.ai ledger APIs.

<a id="plugins.aea-ledger-fetchai.aea_ledger_fetchai.fetchai.FetchAIApi.contract_method_call"></a>

#### contract`_`method`_`call

