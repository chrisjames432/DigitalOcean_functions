# DigitalOcean Functions

A way to interact with Digital Ocean serverless functions.

You will need a .env file with your Digital Ocean API key.

## Installation and Configuration

### Install and Configure doctl on Linux

1. **Install doctl**:
   - Download doctl from the [Releases page](https://github.com/digitalocean/doctl/releases).
   - Extract the binary and move it to your PATH.
     ```sh
     cd ~
     wget https://github.com/digitalocean/doctl/releases/download/v1.104.0/doctl-1.104.0-linux-amd64.tar.gz
     tar xf ~/doctl-1.104.0-linux-amd64.tar.gz
     sudo mv ~/doctl /usr/local/bin
     ```

2. **Create and Use API Token**:
   - Create an API token from the DigitalOcean control panel with read and write access.
   - Initialize doctl with the API token.
     ```sh
     doctl auth init --context <NAME>
     doctl auth list
     doctl auth switch --context <NAME>
     ```

3. **Validate doctl**:
   - Check account details and create a droplet.
     ```sh
     doctl account get
     doctl compute droplet create --region sfo2 --image ubuntu-23-10-x64 --size s-1vcpu-1gb <DROPLET-NAME>
     doctl compute image list
     doctl compute droplet delete <DROPLET-ID>
     ```

4. **Install Serverless Functions Support (Optional)**:
   - Install the serverless extension.
     ```sh
     doctl serverless install
     ```

## Functions Quickstart

1. **Command Line Setup**:
   - Ensure doctl is installed and authorized with serverless extension.
     ```sh
     doctl version
     doctl serverless status
     ```

2. **Create a Namespace**:
   - List available regions and create a namespace.
     ```sh
     doctl serverless namespaces list-regions
     doctl serverless namespaces create --label example-namespace --region nyc1
     ```

3. **Create and Deploy a Function**:
   - Initialize a sample project and deploy the function.
     ```sh
     doctl serverless init --language js <example-project>
     doctl serverless deploy <example-project>
     ```

4. **Invoke and Customize the Function**:
   - Invoke the deployed function and customize the greeting.
     ```sh
     doctl serverless functions invoke sample/hello
     doctl serverless functions invoke sample/hello -p name:sammy
     ```

5. **Destroy a Function**:
   - Remove functions from the cloud.
     ```sh
     doctl serverless undeploy sample/hello
     ```

Your function is now undeployed from Functions.