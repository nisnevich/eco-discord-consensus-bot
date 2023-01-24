from enum import Enum

LOG_PATH = "logs/lazy-consensus-bot.log"
TESTS_PATH = "tests/"
LOG_FILE_SIZE = 1024 * 1024 * 10

DB_NAME = "lazy-consensus-bot.db"
GRANT_PROPOSALS_TABLE_NAME = "grant_proposals"
VOTERS_TABLE_NAME = "voters"

# FIXME change values back after testing
GRANT_PROPOSAL_TIMER_SECONDS = 20
GRANT_PROPOSAL_TIMER_SLEEP_SECONDS = 1
#  GRANT_PROPOSAL_TIMER_SECONDS = 259200  # 3 days
#  GRANT_PROPOSAL_TIMER_SLEEP_SECONDS = 60  # 1 minute

# L3 or Eco role
# FIXME: change roles back to Eco Discord when testing is done
ROLE_IDS_ALLOWED = (1063903240925749389,)
# ROLE_IDS_ALLOWED = (812675567438659624, 1038497110754086913)

DISCORD_COMMAND_PREFIX = "!"
RESPONSIBLE_MENTION = "<@703574259401883728>"  # Nickname of a person who's responsible for maintaining the bot (used in some error messages to ping).
REACTION_ON_BOT_MENTION = "👋"  # wave
GRANT_PROPOSAL_COMMAND_NAME = 'propose'
CANCEL_EMOJI_UNICODE = "\U0000274C"  # ❌ (:x: emoji)
VOTING_CHANNEL_ID = "1067119414731886645"
LAZY_CONSENSUS_THRESHOLD = 8


class ProposalResult(Enum):
    ACCEPTED = 0
    CANCELLED_BY_REACHING_THRESHOLD = 1
    CANCELLED_BY_PROPOSER = 2


# ==============
# Messages texts
# ==============
COMMAND_FORMAT_RESPONSE = """
Hi {author}! This command should look like:

`!propose @username amount description`

> @username - the user you would like to reward.
> amount - how many points you would like to give.
> description - a text that should explain for others what the grant is given for (this is required). If the grant will be applied, I'll post this message.

Some examples:
!propose {author} 100 for being awesome
!propose {author} 100 for using Lazy Consensus bot
"""
# validation.py error messages
ERROR_MESSAGE_NO_MENTIONS = (
    "No mentions found. Please mention the user you want to propose the grant to."
)
ERROR_MESSAGE_INVALID_COMMAND_FORMAT = (
    "The mention must follow after `!propose `. Example: `!propose @mention`."
)
ERROR_MESSAGE_INVALID_USER = "Unable to resolve username. Is the user on this Discord server?"
ERROR_MESSAGE_INVALID_AMOUNT = (
    "The amount must be a positive integer. Example: `!propose @mention 100`."
)
ERROR_MESSAGE_NEGATIVE_AMOUNT = "The amount must be a positive integer: {amount}"
ERROR_MESSAGE_INVALID_DESCRIPTION = (
    "Please provide a description of the grant, like this: `!propose @mention amount description`."
)
# Proposal related public messages
NEW_PROPOSAL_SAME_CHANNEL_RESPONSE = """
Alright, let's make this happen! You're proposing to give {mention} {amount} points, but watch out! If {threshold} or more big wigs (Layer 3) vote against it, the deal's off. Anyone who objects can make their voices heard here: {voting_link}
"""
NEW_PROPOSAL_VOTING_CHANNEL_MESSAGE = """
:rocket: {countdown} will grant {amount} points to {mention} as proposed by {author}, unless {threshold} members react with {reaction} to this message before {date_finish}.
Goal: {description}
"""  # Another version: {author} proposed giving {amount} points to {mention}. {threshold} votes against will cancel it. Use {reaction} to vote before {date_finish}.
PROPOSAL_RESULT_VOTING_CHANNEL_EDITED_MESSAGE = """
The {amount} point proposal for {mention} by {author} has come to a close. {result}
Goal: {description}
The original proposal: {link_to_original_message}
"""
PROPOSAL_RESULT_VOTING_CHANNEL = {
    "Accepted": "The grant has been given!",
    "CancelledByReachingThreshold": "The proposal has been cancelled due to opposition from {threshold} members: {voters_list}",
    "CancelledByProposer": "The proposal has been cancelled by the proposer.",
}
PROPOSAL_RESULT_PROPOSER_RESPONSE = {
    "Accepted": "Hooray! The grant has been given and {mention} is now richer by {amount} points!",
    "CancelledByReachingThreshold": "Sorry, {author}, but it looks like {threshold} members
    weren't on board with your proposal: {voting_link}",
    "CancelledByProposer": "Oh well, {author} has cancelled the proposal.",
}
