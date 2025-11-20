# Credit @ph0enix_web.
# Maintained by @ph0enix_web
# New maintainer @ph0enix_web
# Thank you to the original developer for the base code.
# Credit to the original developer.
# For support, contact @ph0enix_web on Telegram. 
# This is a free and open-source project.
def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'
