# Credit @ph0enix_web.
# Maintained by @ph0enix_web
# New maintainer @ph0enix_web
# Thank you to the original developer for the base code.
# Credit to the original developer.
# For support, contact @ph0enix_web on Telegram. 
# This is a free and open-source project.
def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string representation of bytes """
    return str(bytes) + units[0] if int(bytes) < 1024 else human_size(int(bytes)>>10, units[1:])
