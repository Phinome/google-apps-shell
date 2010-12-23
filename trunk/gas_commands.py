# gas_commands.py
#
# Documentation for the GAS commands.

__version__ = '1.1.0'

commands = {

  'create_user': {
    'title': 'Creating a User',
    'category': 'Users',
    'usage': 'gas create_user user_name=<name> first_name=<First Name> last_name=<Last Name> password=<Password> [password_hash_function=SHA-1|MD5] [suspended=true|false] [quota_limit=<quota size>] [change_password=true|false]',
    'description': """
Creates a user account named user_name, with name first_name and last_name, and password password. These fields should be quoted if they contain spaces.
Optional parameter password_hash_function tells GAS that the password is being already given in an encrypted format, either SHA-1 or MD5.
Optional parameter suspended creates the account but marks it as suspended.
Optional parameter quota allows you to set the user's email quota.
Optional parameter change_password will force the user to change their password after their first successful login.
""",
    'examples': [
      ('gas create_user user_name=monkey first_name=David last_name=Monkey password=ILikeBananas',
      'This example creates a user account.'),
      ('gas create_user user_name=elephant@secondarydomain.com first_name=Big last_name=Ears password=ILikePeanuts',
      'This example creates a user in a secondary domain. This is useful when a Google Apps account has multiple domains.')
      ]
  },
  
  'update_user': {
    'title': 'Update (and Rename) a User',
    'category': 'Users',
    'usage': 'gas update_user user_name=<name> [new_user_name=<New Name>] [first_name=<First Name>] [last_name=<Last Name>] [password=<Password>] [password_hash_function=SHA-1|MD5] [suspended=true|false] [quota_limit=<quota size>] [change_password=true|false] [admin=true|false] [suspended=true|false] [ip_whitelisted=true|false]',
    'description': """
Updates the user account for user_name. All parameters except user_name are optional. If you wish to rename the username for this user, set new_user_name.

Google makes the following recommendations when renaming a user account:

    * Before renaming a user, it is recommended that you logout the user from all browser sessions and services. For instance, you can get the user on your support desk telephone line during the rename process to ensure they have logged out. The process of renaming can take up to 10 minutes to propagate across all services.
    * Google Talk will lose all remembered chat invitations after renaming. The user must request permission to chat with friends again.
    * When a user is renamed, the old username is retained as a nickname to ensure continuous mail delivery in the case of email forwarding settings and will not be available as a new username. If you prefer not to have the nickname in place after the rename, you'll need to Delete the Nickname 
""",
    'examples': [
      ('gam update_user user_name=jack first_name=Jack last_name=Johnson password=MovingOut admin=true suspended=false',
      'This example updates a user account, setting the first_name, last_name and password and making them an administrator.'),
      ('gam update_user user_name=jeffrey new_user_name=jeff',
      'This example renames the user jeffrey to jeff.')
      ]
  },
  
  'read_user': {
    'title': 'Get User Info',
    'category': 'Users',
    'usage': 'gas read_user user_name=<name>',
    'description': """
Retrieve details about the given user.
""",
    'examples': [
      ('gas read_user user_name=daniel',
      'This example will show information on the user daniel.')
      ]
  },
  
  'delete_user': {
    'title': 'Delete a User',
    'category': 'Users',
    'usage': 'gas delete_user user_name=<name> [no_rename=true]',
    'description': """
Delete the given user's account. GAS will first rename the user with the current timestamp and then delete the account. This allows the user to be recreated immediately rather than waiting the 5 days that Google normally requires. 
""",
    'examples': [
      ('gas delete_user user_name=igotfired no_rename=true',
      'This example will delete the account for user igotfired without first renaming the account.')
      ]
  },
  
  'suspend_user': {
    'title': 'Suspend a User',
    'category': 'Users',
    'usage': 'gas suspend_user user_name=<name>',
    'description': """
Suspends the given user's account.
""",
    'examples': [
      ('gas suspend_user user_name=iamsuspended',
      'This example suspend the account for user iamsuspended. Suspended accounts can be restored at a later date.')
      ]
  },
  
  'rename_user': {
      'title': 'Rename a User',
      'category': 'Users',
      'usage': 'gas rename_user user_name=<name> new_user_name=<name>',
      'description': """
  Renames the user_name account to new_user_name. Note that the user's primary calendar name must still be changed manually.
""",
      'examples': [
        ('gas rename_user user_name=christopher new_user_name=chris',
        'This example renames the user christopher to chris.')
        ]
    },

  'restore_user': {
    'title': 'Restore a User',
    'category': 'Users',
    'usage': 'gas restore_user user_name=<name>',
    'description': """
Restores a user (from a suspended user state). 
""",
    'examples': [
      ('gas restore_user user_name=ihavereturned',
      'This example restores the user ihavereturned, in the case that ihavereturned was suspended earlier.')
      ]
  },

  'print_authentication': {
    'title': 'Print Authentication',
    'category': 'Authentication',
    'usage': 'gas print_authentication',
    'description': """
Prints out the current GAS authentication status, telling you whether you are logged in, and who you are logged in as.
""",
    'examples': [
      ('gas print_authentication',
      'This example prints out the current authentication status.')
      ]
  },
  
  'create_label': {
      'title': 'Create Label',
      'category': 'Email Settings',
      'usage': 'gas create_label user_name=<name> label=<label>',
      'description': """
Creates a new label for user_name.
""",
      'examples': [
        ('gas create_label user_name=jeff label=Chrome',
        'This example creates a label for jeff@mydomain.com named Chrome.')
        ]
  },
    
  'create_filter': {
      'title': 'Create Filter',
      'category': 'Email Settings',
      'usage': 'gas create_filter user_name=<name> [mail_from=<name>] [mail_to=<name>] [subject=<subject>] [has_the_word=<words>] [does_not_have_the_word=<words>] [has_attachment=<bool>] [label=<label>] [should_mark_as_read=<bool>] [should_archive=<bool>]',
      'description': """
Creates a filter on behalf of user_name.  Optional parameters include: mail_from, mail_to, subject, has_the_word, does_not_have_the_word, has_attachment. Actions include label, should_mark_as_read, and should_archive.
""",
      'examples': [
        ('gas create_filter user_name=jeff mail_from=sandra has_attachment=true label=Sandy should_archive=true',
        'This example creates a filter for user jeff, labelling all mail from sandra with an attachment, and skipping the inbox by archiving the email.')
        ]
  },
    
  'create_send_as': {
      'title': 'Create Send As Alias',
      'category': 'Email Settings',
      'usage': 'gas create_send_as user_name=<email> name=<name> address=<email> [reply_to=<email>] [make_default=true|false]',
      'description': """
Creates a send as alias on behalf of user_name. This allows the user user_name to send email as "name <address>" with an optional reply to.
""",
      'examples': [
        ('create_send_as user_name=tim name="Timothy Johnson" address=timothy@domain.com reply_to=tim@domain.com',
        'This example creates a send as alias for tim, allowing him to send as Timothy Johnson with timothy@domain.com.')
        ]
  },
  
  'update_web_clips': {
      'title': 'Update Web Clips',
      'category': 'Email Settings',
      'usage': 'gas update_web_clips user_name=<name> enable=<bool>',
      'description': """
Enables or disables web clips for a user.
""",
      'examples': [
        ('gas update_web_clips user_name=ben enable=false',
        'This example turns off web clips for a user.')
        ]
  },

  'update_forwarding': {
    'title': 'Update Forwarding Mail',
    'category': 'Email Settings',
    'usage': 'gas update_forwarding user_name=<name> enable=<bool> [enable_for=<name>] [action=keep|archive|delete]',
    'description': """
If enable is true, this creates a forwarding rule for user_name, forwarding all incoming mail to enable_for. Action describes what should happen to the email afterward. It'll either remain in the inbox, get archived, or get deleted. If enable is false, this disables any existing forwarding rule.
""",
    'examples': [
      ('gas update_forwarding user_name=sales enable=true forward_to=kyle@mydomain.com action=archive',
      'This example forwards all mail for sales@mydomain.com to kyle@mydomain.com.')
      ]
  },
  
  'update_pop': {
      'title': 'Update POP Access',
      'category': 'Email Settings',
      'usage': 'gas update_pop user_name=<name> enable=<bool> enable_for=[all_mail|mail_from_now_on] action=[keep|archive|delete]',
      'description': """
Enables or disables POP access for user_name. Parameter enable_for determines whether POP access is enabled from now on or for all mail. Action describes what should happen to the email afterward.
""",
      'examples': [
        ('gas update_pop user_name=ken enable=true enable_for=all_mail action=delete',
        'This example turns on POP access for user ken, for all mail, instructing Google to delete the mail after it has been accessed.')
        ]
  },
  
  'update_imap': {
      'title': 'Update IMAP Access',
      'category': 'Email Settings',
      'usage': 'gas update_imap user_name=<name> enable=<bool>',
      'description': """
Enables or disables IMAP access for user_name.
""",
      'examples': [
        ('gas update_imap user_name=admin enable=true',
        'This example enables IMAP access for user ken.')
        ]
  },
  
  'update_vacation': {
      'title': 'Update Vacation Responder',
      'category': 'Email Settings',
      'usage': 'gas update_vacation user_name=<name> enable=<bool> [subject=<subject>] [message=<message>] [contacts_only=<bool>]',
      'description': """
Creates or disables automatic vacation responder for user_name. If the vacation responder is being created, contacts_only describes whether the vacation alert should only be emailed to users in user_name's personal contacts.
""",
      'examples': [
        ('gas update_vacation user_name=gonesurfing enable=true subject="OOO - Hawaii for Thanksgiving" message="I am out-of-office (Hawaii) and will be slow to respond to email. Aloha!" contacts_only=false',
        'This example creates an automatic vacation responder that will get sent to anyone who emails gonesurfing@domain.com.')
        ]
  },
  
  'update_signature': {
      'title': 'Update Signature',
      'category': 'Email Settings',
      'usage': 'gas update_signature user_name=<name> signature=<signature>',
      'description': """
Sets the user's signature to signature. Use \\n for new lines.
""",
      'examples': [
        ('gas update_signature user_name=bill signature="Bill Johnson\\nDirect line: 1-800-123-4567.',
        'This example sets a signature.')
        ]
  },

  'update_language': {
      'title': 'Update Language',
      'category': 'Email Settings',
      'usage': 'gas update_language user_name=<name> language=<language>',
      'description': """
Sets the user's language preference to language. Some common language codes are en-US for American English, en-GB for British English, fr for French, and es for Spanish. For a full list of language codes, see http://code.google.com/googleapps/domain/email_settings/developers_guide_protocol.html#GA_email_language_tags
""",
      'examples': [
        ('gas update_language user_name=pierre language=fr',
        'This example sets the language preference to French.')
        ]
  },
    
  '_TEMPLATE': {
      'title': '',
      'category': '',
      'usage': '',
      'description': """
  
""",
      'examples': [
        ('',
        '')
        ]
  }
}
