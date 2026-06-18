# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def thesaurusly(sentence, synonyms):
  words = sentence.split()
  res = []
  cur_sentence = []

  def visit(i):
    if i == len(words):
      res.append(" ".join(cur_sentence))
      return

    if words[i] not in synonyms:
      choices = [words[i]]
    else:
      choices = synonyms.get(words[i], [])

    for choice in choices:
      cur_sentence.append(choice)
      visit(i + 1)
      cur_sentence.pop() # Undo change.

  visit(0)
  return res