# DigitalOcean_functions
A way to interact with Digital Ocean serverless functions.


You will need a .env with Digital ocean api key


## How to Install and Configure doctl on Linux

**Validated on 15 Apr 2020 • Last edited on 8 May 2024**

### Step 1: Install doctl

1. **Download doctl**:
   Visit the [Releases page](https://github.com/digitalocean/doctl/releases) for the doctl GitHub project and find the appropriate archive for your Linux system. Download the archive using wget:

   ```sh
   cd ~
   wget https://github.com/digitalocean/doctl/releases/download/v1.104.0/doctl-1.104.0-linux-amd64.tar.gz
   ```

2. **Extract the binary**:
   ```sh
   tar xf ~/doctl-1.104.0-linux-amd64.tar.gz
   ```

3. **Move the binary to your PATH**:
   ```sh
   sudo mv ~/doctl /usr/local/bin
   ```

### Step 2: Create an API Token

1. **Create an API Token**:
   - Go to the Applications & API page in the DigitalOcean control panel.
   - Create a token with read and write access.
   - Save the token in a safe place as it is displayed only once.

### Step 3: Use the API Token to Grant Account Access to doctl

1. **Initialize doctl with the API token**:
   If you installed doctl using the Ubuntu Snap package, first create the user configuration directory:
   ```sh
   mkdir ~/.config
   ```

2. **Authenticate doctl**:
   ```sh
   doctl auth init --context <NAME>
   ```

   You can switch between multiple authenticated accounts:
   ```sh
   doctl auth list
   doctl auth switch --context <NAME>
   ```

### Step 4: Validate that doctl is Working

1. **Check account details**:
   ```sh
   doctl account get
   ```

   Expected output:
   ```
   Email                      Droplet Limit    Email Verified    UUID                                        Status
   sammy@example.org          10               true              3a56c5e109736b50e823eaebca85708ca0e5087c    active
   ```

2. **Create a Droplet**:
   ```sh
   doctl compute droplet create --region sfo2 --image ubuntu-23-10-x64 --size s-1vcpu-1gb <DROPLET-NAME>
   ```

3. **List available Droplet images**:
   ```sh
   doctl compute image list
   ```

4. **Delete a Droplet**:
   ```sh
   doctl compute droplet delete <DROPLET-ID>
   ```

   Confirm deletion by typing `y` when prompted.

### Step 5: Install Serverless Functions Support (Optional)

1. **Install the serverless extension**:
   ```sh
   doctl serverless install
   ```

   The installation process:
   ```
   Downloading...Unpacking...Installing...Cleaning up...
   Done
   ```

2. **Get started with Functions**:
   - Create a namespace.
   - Deploy your functions.
   - See the Functions Quickstart for more details..
