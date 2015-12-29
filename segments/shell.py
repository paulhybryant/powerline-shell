def add_shell_segment(powerline):

    if powerline.args.shell == 'bash':
        shell_prompt = ' bash'
    elif powerline.args.shell == 'zsh':
        shell_prompt = ' zsh'
    else:
        shell_prompt = ' ?sh'

    powerline.append(shell_prompt, Color.SHELL_FG, Color.SHELL_BG)
