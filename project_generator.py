import os

def create_project_structure(project_name, framework_choice):
    # Define the structure of directories and files based on the choice
    if framework_choice == '1':
        framework = 'aiogram'
        structure = [
            project_name,
            os.path.join(project_name, 'handlers'),
            os.path.join(project_name, 'middlewares'),
            os.path.join(project_name, 'models'),
            os.path.join(project_name, 'utils'),
            os.path.join(project_name, 'config.py'),
            os.path.join(project_name, 'main.py'),
            os.path.join(project_name, 'requirements.txt'),
            os.path.join(project_name, 'README.md'),
            os.path.join(project_name, 'handlers', '__init__.py'),
            os.path.join(project_name, 'middlewares', '__init__.py'),
            os.path.join(project_name, 'models', '__init__.py'),
            os.path.join(project_name, 'utils', '__init__.py'),
        ]
    elif framework_choice == '2':
        framework = 'aiogram+telethon'
        structure = [
            project_name,
            os.path.join(project_name, 'handlers'),
            os.path.join(project_name, 'middlewares'),
            os.path.join(project_name, 'models'),
            os.path.join(project_name, 'utils'),
            os.path.join(project_name, 'config.py'),
            os.path.join(project_name, 'main.py'),
            os.path.join(project_name, 'requirements.txt'),
            os.path.join(project_name, 'README.md'),
            os.path.join(project_name, 'telethon_client.py'),
            os.path.join(project_name, 'handlers', '__init__.py'),
            os.path.join(project_name, 'middlewares', '__init__.py'),
            os.path.join(project_name, 'models', '__init__.py'),
            os.path.join(project_name, 'utils', '__init__.py'),
        ]
    else:
        print("Unknown choice. Use '1' for aiogram or '2' for aiogram+telethon.")
        return

    # Create directories and files
    for path in structure:
        if path.endswith('.py') or path.endswith('.txt') or path.endswith('.md'):
            # Create files with basic functionality
            with open(path, 'w') as f:
                if path == os.path.join(project_name, 'config.py'):
                    f.write("# Bot configuration\n")
                    f.write("TOKEN = 'your_bot_token'\n")
                elif path == os.path.join(project_name, 'main.py'):
                    f.write("# Main file to run the bot\n")
                    f.write("from aiogram import Bot, types\n")
                    f.write("from aiogram import F\n")
                    f.write("from aiogram import Router\n")
                    f.write("from aiogram.utils import executor\n")
                    f.write("import config\n\n")
                    f.write("bot = Bot(token=config.TOKEN)\n")
                    f.write("router = Router()\n\n")
                    f.write("@router.message(F.text & F.command('start'))\n")
                    f.write("async def send_welcome(message: types.Message):\n")
                    f.write("    await message.answer('Hello!')\n\n")
                    f.write("if __name__ == '__main__':\n")
                    f.write("    executor.start_polling(bot, router, skip_updates=True)\n")
                elif path == os.path.join(project_name, 'requirements.txt'):
                    f.write("aiogram==3.*\n")
                    if framework == 'aiogram+telethon':
                        f.write("telethon\n")
                elif path == os.path.join(project_name, 'README.md'):
                    f.write("# " + project_name + "\n")
                    f.write("## Project Description\n")
                    f.write("This project is a bot based on " + framework + ".\n")
                else:
                    f.write("# This package contains handlers for " + framework + ".\n")
            print(f"Created file: {path}")
        else:
            # Create directories
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    print("Choose a framework:")
    print("1. aiogram")
    print("2. aiogram + telethon")
    framework_choice = input("Enter framework number: ")
    create_project_structure(project_name, framework_choice)
