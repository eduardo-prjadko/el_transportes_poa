# Extract and Load procedure 

The current repo is a simple extract and load procedure mounted on an Azure Functions structure. Since it doesn't cover the transform step of a classic ELT pipeline, this app simply downloads the entire data of the public API https://dadosabertos.poa.br/api/3/action/datastore_search?resource_id=cb96a73e-e18b-4371-95c5-2cf20e359e6c (no credentials required) and stores it in a storage container. 

# installation

The step by step installation guide will cover the installation trough VSCode integration with Azure Functions. For a guide about development environment setup, please, follow the steps in [this tutorial](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=python). After completing the tutorial, you will be ready to install the **el_transportes_poa**.

### **Clone repository**
Create and open a folder in VSCode. Open the terminal in VSCode and clone the repository to the current folder:

```python
git clone https://github.com/eduardo-prjadko/el_transportes_poa.git .
```
### **Upload to Azure Functions**
In the Azure Functions extension tab, refresh the functions workspace so that the extension can identfy the project on the *Local Project* folder.
<br>
![local project example](images/el_project.png "local project")
<br>
Deploy the local project, as it is, to an existing function or create a new, following the instructions in VSCode.

### **Setup the environment variables**
The required environment variables for the app are two:
* LIMIT - number of rows retrieved from endpoint
* CONTAINER - the name of the azure storage container where data will be saved. There is no need the previously create the container, since the app automatocally creates it.

It can be set in VSCode or Azure Portal. FOr more information about setting environment variables on Azure Functions follow [this link](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal).
<br><br>
> Obs: for unit testing purpose, it is needed to set the environment variable AzureWebJobsStorage, which points to the storage connection string found in Azure Portal.