# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class SimpleTextEditor:
  def __init__(self):
    self.text = []
    self.undo_stack = []
    self.redo_stack = []

  def append(self, c):
    self.undo_stack.append(('append', c))
    self.text.append(c)
    self.redo_stack.clear()  # Clear redo stack on new operation

  def backspace(self):
    if not self.text:
      return
    c = self.text.pop()
    self.undo_stack.append(('backspace', c))
    self.redo_stack.clear()  # Clear redo stack on new operation

  def undo(self):
    if not self.undo_stack:
      return
    op, c = self.undo_stack.pop()
    if op == 'append':
      self.text.pop()
      self.redo_stack.append(('append', c))
    else:  # backspace
      self.text.append(c)
      self.redo_stack.append(('backspace', c))

  def redo(self):
    if not self.redo_stack:
      return
    op, c = self.redo_stack.pop()
    if op == 'append':
      self.text.append(c)
      self.undo_stack.append(('append', c))
    else:  # backspace
      self.text.pop()
      self.undo_stack.append(('backspace', c))

  def display(self):
    return "".join(self.text)