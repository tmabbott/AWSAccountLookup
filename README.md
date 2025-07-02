# AWSAccountLookup

by Tim Mabbott

This is a super simple Automator workflow to add a quick AWS account lookup action to a key-combo.

## Steps to install

- donwload this repo
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
- trigger your key-combo
- Alternatively you can Ctrl-Click-(on the highlighted number)->Services->AWS Account Lookup

## Contributing/Feedback

Coming soon.

