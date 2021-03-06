class ActiveCalls:
    def __init__(self, pytgcalls):
        self.pytgcalls = pytgcalls

    @property
    def calls(self):
        return self.pytgcalls._calls

    @property
    def num_calls(self):
        return len(self.calls)

    def _add_call(self, chat_id: int):
        if chat_id not in self.calls:
            self.pytgcalls._calls.append(chat_id)

    def _rm_call(self, chat_id: int):
        if chat_id in self.calls:
            self.pytgcalls._calls.remove(chat_id)

    @property
    def active_calls(self):
        return self.pytgcalls._active_calls

    @property
    def num_active_calls(self):
        return len(self.active_calls)

    def _add_active_call(self, chat_id: int):
        if chat_id not in self.active_calls:
            self.pytgcalls._active_calls[chat_id] = 'playing'

    def _rm_active_call(self, chat_id: int):
        if chat_id in self.active_calls:
            del self.pytgcalls._active_calls[chat_id]

    def _set_status(self, chat_id: int, status: str):
        if chat_id in self.active_calls:
            self.pytgcalls._active_calls[chat_id] = status
