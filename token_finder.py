class CsrfToken:
    def __init__(self, bs4_forms_list):
        self.name = ''
        self.value = ''
        self.forms_list = bs4_forms_list

        for _form in self.forms_list:
            _inputs = _form.findAll('input')
            for _input in _inputs:
                if _input.get('type') == 'hidden':
                    self.value = _input.get('value')
                    self.name = _input.get('name')

