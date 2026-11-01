# Getting Started with the MLOps Assignment 2

Welcome! This guide will help you get up and running with the LLMOps assignment. We've tried to make it as simple as possible, so you can focus on learning rather than troubleshooting setup issues.

## Your First Time? Start Here

Getting everything set up takes just a few minutes. We've automated most of the heavy lifting for you.

### Step 1: Run the Setup Script

The first thing you'll do is run a setup script. This might sound complicated, but it's really just one command:

```bash
bash setup.sh
```

This script is smart enough to figure out what operating system you're using (whether you're on a Mac or Rocky Linux), and it will do all the work from there. It creates a Python virtual environment, downloads and installs all the packages you need, sets up your project folders, and gets your configuration file ready.

The script will also talk to you as it goes, letting you know what it's doing and whether anything goes wrong. If you've already run this once and you're running it again, it'll ask you before overwriting anything important.

### Step 2: Add Your OpenAI API Key

After the setup script finishes, you need to add your API key. This is what lets you use the OpenAI API. Open your configuration file in a text editor:

```bash
nano .env
```

Then add your key. It should look something like this:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
```

Don't have a key yet? Read OPENAI_API_KEY_SETUP.md. It walks you through creating an account, generating your key, and managing your costs.

### Step 3: Verify Your Setup

Before you start working, it's a good idea to verify that everything installed correctly. We have a verification script that checks 20 different things:

```bash
bash verify_setup.sh
```

This checks that your Python version is compatible, all the packages are installed, your configuration file is set up correctly, and all the project files are where they should be. If anything's missing, it'll tell you exactly what needs to be fixed.

### Step 4: Activate Your Environment and Run the Project

Now you're ready to go. First activate your environment:

```bash
bash activate.sh
```

Then fire up the Jupyter notebook:

```bash
jupyter notebook llmops_assignment.ipynb
```

Your browser will open, and you'll see the notebook with all 20 cells ready to run. Just start with the first cell and work your way through them in order.

## If You're Coming Back Later

If you've already done the setup and you're just coming back to work on the project again, you can skip the setup step. Just do this:

```bash
bash activate.sh
jupyter notebook llmops_assignment.ipynb
```

That's it. The activation script will remind you of what you can do and what comes next.

## What's This Assignment Actually About?

The assignment has three parts that work together:

**First, you'll measure how fast the API responds.** You'll call GPT-3.5 with different versions of prompts and track how long each request takes. This helps you understand the performance of different approaches.

**Second, you'll calculate costs.** You'll count how many tokens each prompt uses and figure out what it would cost to run these prompts at scale. API costs add up quickly, so this is important stuff.

**Third, you'll experiment with MLflow.** You'll register different prompt versions, run experiments on them, and compare their performance. This is where you figure out which version actually works best.

All three parts connect together in the notebook, so doing them in order makes sense. By the end, you'll have measurements, cost projections, and experiment data showing which prompt version performs best.

## What Will You Have When You're Done?

After you run the notebook, you'll have several things:

- A CSV file with latency measurements showing how fast each prompt version responded
- Another CSV with cost calculations and token usage data
- MLflow experiment data that you can explore visually
- Screenshots showing the experiments and results

All of this is what you'll need to submit with your assignment, and we've set it up so the notebook creates all of this automatically.

## Something Not Working? We Can Help

We built in a system to help you figure out what went wrong. If something doesn't seem right, just run the verification script:

```bash
bash verify_setup.sh
```

It will check everything and tell you exactly what's missing or broken. The output is designed to be helpful, not just show you an error message.

If you need more detailed help, we have documentation for pretty much every scenario. Quick command reference, detailed setup guides for different operating systems, help with API keys, complete documentation - it's all there.

## Getting Around the Documentation

Here's where to go depending on what you need:

- **New to this and not sure where to start?** This guide (START_HERE.md) is what you're reading
- **Want just the commands without all the explanation?** Check out QUICK_START.md
- **Setting this up on Rocky Linux?** See ROCKY_LINUX_SETUP.md
- **Need help with your API key?** Read OPENAI_API_KEY_SETUP.md

## Your Next Move

Just pick the command that matches where you are:

If this is your first time:
```bash
bash setup.sh
```

If you've already set up and you're coming back:
```bash
bash activate.sh
jupyter notebook llmops_assignment.ipynb
```

If you want to check that everything's installed:
```bash
bash verify_setup.sh
```

If you want to see the MLflow results:
```bash
mlflow ui --port 5000
```

Take it one step at a time. You'll be up and running faster than you think!
