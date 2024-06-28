## Functions Quickstart

**Validated on 23 May 2022 • Last edited on 29 Sep 2023**

Functions are blocks of code that run on demand without the need to manage any infrastructure. Develop on your local machine, test your code from the command line (using doctl), then deploy to a production namespace or App Platform — no servers required.

You can start writing a function using either the doctl command line tool or our control panel. The control panel is great for experimentation, but a command line workflow is the intended route for in-depth development of functions.

### Command Line Setup

1. **Install and Authorize doctl**:
   - Make sure you have doctl installed, authorized to access your DigitalOcean account, and set up with the serverless extension. See [How To Install and Configure doctl](#) for instructions.

2. **Check doctl Version**:
   - Ensure you have doctl version 1.81.0 or higher:
     ```sh
     doctl version
     ```

3. **Check Serverless Extension**:
   - Verify the serverless extension is installed:
     ```sh
     doctl serverless status
     ```
   - The output should indicate that serverless support is installed but not connected to a functions namespace:
     ```
     Error: serverless support is installed but not connected to a functions namespace (use `doctl serverless connect`)
     ```

### Create a Namespace

Namespaces are a way of organizing and isolating functions and their settings. You may have Production and Development namespaces, or project-based namespaces.

1. **List Available Regions**:
   ```sh
   doctl serverless namespaces list-regions
   ```

2. **Create a Namespace**:
   ```sh
   doctl serverless namespaces create --label example-namespace --region nyc1
   ```
   - This command creates a namespace called `example-namespace` in the `nyc1` region and automatically connects to it:
     ```
     Connected to functions namespace 'fn-ef552165-54d2-4656-b6b1-7dedc370591a' on API host 'https://faas-nyc1-2ef2e6cc.doserverless.co'
     ```

### Create a Local Function Directory

1. **Initialize a Sample Project**:
   - Navigate to your desired directory and initialize a sample project:
     ```sh
     doctl serverless init --language js <example-project>
     ```
   - Replace `<example-project>` with your project name. A directory will be created with sample code and configuration files:
     ```
     A local functions project directory 'example-project' was created for you.
     ```

2. **Project Directory Structure**:
   - The directory will contain a `project.yml` file and a `packages` directory with sample code:
     ```
     example-project/
     ├── packages
     │   └── sample
     │       └── hello
     │           └── hello.js
     └── project.yml
     ```

### Deploy a Function

1. **Deploy the Function**:
   - Deploy the sample “hello world” function:
     ```sh
     doctl serverless deploy <example-project>
     ```
   - Replace `<example-project>` with your project name. The command will output deployment details:
     ```
     Deploying '/home/sammy/example-project'
       to namespace 'fn-feb132ee-706a-4f13-9c81-f24a3330260b'
       on host 'https://faas-nyc1-78edc.doserverless.co'
     Deployment status recorded in '.deployed'

     Deployed functions ('doctl sbx fn get <funcName> --url' for URL):
       - sample/hello
     ```

### Invoke a Function

1. **Invoke the Deployed Function**:
   - Use the following command to invoke the function:
     ```sh
     doctl serverless functions invoke sample/hello
     ```
   - The function will return a JSON response:
     ```json
     {
       "body": "Hello stranger!"
     }
     ```

2. **Customize the Greeting**:
   - Add key:value parameters to customize the greeting:
     ```sh
     doctl serverless functions invoke sample/hello -p name:sammy
     ```
   - The response will be customized:
     ```json
     {
       "body": "Hello sammy!"
     }
     ```

### Destroy a Function

1. **Remove Functions from the Cloud**:
   - Use the following command to undeploy a function:
     ```sh
     doctl serverless undeploy sample/hello
     ```
   - The command will verify the process was successful:
     ```
     The requested resources have been undeployed
     ```

Your function is now undeployed from Functions.