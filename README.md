# AWSAccountLookup

by Tim Mabbott

If you work with a resonable number of AWS accounts you will very likely end up seeing account IDs in a context that doesn't include the account name.  This can be annoying, so I wrote this very simple MacOS Automator workflow to help.  You can simply highlight the ID and hit a key combo to display the assiciated account name.

## Steps to install

- Download this repo
- Install the workflow:
  - Honestly, you shouldn't do this without examining the workflow in Automator (unless you know me, and trust me)
  - Double click the "AWS Account Lookup.workflow" and Automator will prompt to install it, or
  - Move it to ~/Library/Services/
- Install a json file with your account mappings to ~/.aws/accountLookup.json
  - see [sample/accountLookup.json](sample/accountLookup.json) for reference.
- Map a key combo to the workflow.
  - System Settings->Keyboard->Keyboard Shortcuts->Services->Text->AWS Account Lookup
  - double click on "none" and enter your combo.  I use cmd-shift-/

## To use

- Highlight an AWS account number anywhere (mail, terminal, wherever)
- Trigger your key-combo
- Alternatively you can Ctrl-Click-(on the highlighted number)->Services->AWS Account Lookup

You should see something like this:

![Image showing the utility in use](images/example.png)

### How do I create the accountLookup.json file?

There is a script in the scripts directory that will produce a file for you.  It expects a .csv file with column headers of "Account ID" and "Name" (this is what is produced if you do an export from your AWS Org account).

### Won't this file get out of date if I'm creating new accounts?

Yes it will.  If I develop a CLI script to extract the accounts and update the files on a periodic basis, I'll add it to the scripts directory.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing/Feedback

Coming soon.

