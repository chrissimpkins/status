#!/usr/bin/env python
# encoding: utf-8

#------------------------------------------------------------------------------
# status
# Copyright 2014 Christopher Simpkins
# MIT license
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
# c.cmd = Primary command (<executable> <primary command>)
# c.cmd2 = Secondary command (<executable> <primary command> <secondary command>)
#
# c.option(option_string, [bool argument_required]) = test for option with optional positional argument to option test
# c.option_with_arg(option_string) = test for option and mandatory positional argument to option
# c.flag(flag_string) = test for presence of a "option=argument" style flag
#
# c.arg(arg_string) = returns the next positional argument to the arg_string argument
# c.flag_arg(flag_string) = returns the flag assignment for a "--option=argument" style flag
#------------------------------------------------------------------------------------

# Application start
def main():
    import sys
    from Naked.commandline import Command
    from Naked.toolshed.state import StateObject

    #------------------------------------------------------------------------------------------
    # [ Instantiate command line object ]
    #   used for all subsequent conditional logic in the CLI application
    #------------------------------------------------------------------------------------------
    c = Command(sys.argv[0], sys.argv[1:])
    #------------------------------------------------------------------------------
    # [ Instantiate state object ]
    #------------------------------------------------------------------------------
    state = StateObject()
    #------------------------------------------------------------------------------------------
    # [ Command Suite Validation ] - early validation of appropriate command syntax
    # Test that user entered a primary command, print usage if not
    #------------------------------------------------------------------------------------------
    if not c.command_suite_validates():
        from status.commands.usage import Usage
        Usage().print_usage()
        sys.exit(1)
    #------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    #   Enter your command line parsing logic below
    #------------------------------------------------------------------------------------------



    #------------------------------------------------------------------------------------------
    # [ NAKED FRAMEWORK COMMANDS ]
    # Naked framework provides default help, usage, and version commands for all applications
    #   --> settings for user messages are assigned in the lib/status/settings.py file
    #------------------------------------------------------------------------------------------
    elif c.help():  # User requested naked help (help.py module in commands directory)
        from status.commands.help import Help
        Help().print_help()
    elif c.usage():  # user requested naked usage info (usage.py module in commands directory)
        from status.commands.usage import Usage
        Usage().print_usage()
    elif c.version(): # user requested naked version (version.py module in commands directory)
        from status.commands.version import Version
        Version().print_version()
    #------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    # Message to provide to the user when all above conditional logic fails to meet a true condition
    #------------------------------------------------------------------------------------------
    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1) #exit

if __name__ == '__main__':
    main()
