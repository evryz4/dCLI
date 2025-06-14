def args(cmd: str):
    return cmd.split()[1:] if len(cmd.split()) > 1 else ['']

def jargs(cmd: str):
    return ' '.join(args(cmd))