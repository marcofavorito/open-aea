<details><summary>What is an AEA?</summary>
AEA stands for "Autonomous Economic Agent". An AEA can represent an individual, organisation or object and looks after its owner's interests. AEAs act independently of constant user input and autonomously execute actions to achieve their prescribed goals. Their purpose is to create economic value for their owners.
</details>

<details><summary>How do AEAs talk to each other when they do not know each other?</summary>
For an Autonomous Economic Agent (AEA) to talk to other AEAs, it first needs to find them. Once it does, it should ensure that they both use the same protocol for communication, and if so, they then have to send messages to each other.
<br><br>
The AEA framework provides the necessary services to address all three problems. You can read more about the agent communication network <a href="../acn/">here</a>, protocols <a href="../core-components-1/">here</a>, and the Agent Communication Network (ACN) <a href="../acn/">here</a>.
</details>

<details><summary>How does an AEA use blockchain?</summary>
The AEA framework enables agents to interact with blockchains to settle transactions. Currently, the framework has native support for three different networks: <i>Fetch.ai</i>, <i>Ethereum</i> and <i>Cosmos</i>.
<br><br>
You can read more about the framework's integration with the different blockchains <a href="../ledger-integration/">here</a>.
</details>

<details><summary>How does one install third party libraries?</summary>
The framework supports the use of third-party libraries hosted on <a href="https://pypi.org" target="_blank">PyPI</a>. You can directly reference the external dependencies of an AEA package (e.g. skill) in its configuration file. From inside an AEA's project directory, the <code>install</code> command can be used to install all the dependencies of the AEA listed in the configuration files of any of it's packages.
</details>

<details><summary>How does one connect to a database?</summary>
You have two options to connect to a database: using the built-in storage solution or using a custom ORM (object-relational mapping) library and backend.
<br><br>
The use of the built-in storage is explained <a href="../generic-storage/">here</a>. 
</details>

<details><summary>How does one connect a frontend?</summary>
There are multiple options. The most obvious is using an HTTP server connection and creating a client that communicates with this connection. 
<br><br>
You can find a more detailed discussion <a href="../connect-a-frontend/">here</a>.
</details>

<details><summary>Is the AEA framework ideal for agent-based modelling?</summary>
The goal of agent-based modelling (ABM) is to study complex behaviour that emerges as a result of interactions between agents that express well-defined and often simple rule-based behaviour. ABM is a popular technique for studying biological and social systems. Despite some similarities between ABM and the AEA framework, the two serve fundamentally different purposes. ABMs are typically used to study pattern formation at meso and macro scale that result from local agent interactions, whereas in contrast AEAs pursue the owners economic goals. Although possible, the AEA framework offers more complexity than typically is required to address the types of questions ABM is commonly used for. 
<br><br>
You can find more details on the application areas of the AEA framework <a href="../app-areas/">here</a>.
</details>

<details><summary>When a new AEA is created, is the <code>vendor</code> folder populated with some default packages?</summary>
All AEA projects by default hold the <code>open_aea/signing:1.0.0</code> protocols. These (as all other packages installed from the registry) are placed in the <code>vendor</code> folder. 
<br><br>
You can find more details about the file structure <a href="../package-imports/">here</a>.
</details>

<details><summary>Is there a standard for private key files?</summary>
Currently, the private keys are stored in <code>.txt</code> files. This is temporary and will be improved soon.
</details>

<details><summary>How to use the same protocol in different skills?</summary>
The details of envelope/message routing by the AEA framework are discussed in <a href="../message-routing/">this guide</a>.
</details>

<details><summary>Why does the AEA framework use its own package registry?</summary>
AEA packages could be described as personalized plugins for the AEA runtime. They are not like a library - they have no direct use outside the context of the framework - and therefore are not suitable for distribution via <a href="https://pypi.org/" target="_blank">PyPI</a>.
</details>
