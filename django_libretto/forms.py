import django.forms



class FormWithDynamicChoices(django.forms.Form):
	'''
	Add choices to ChoiceFields at the time the form is instantiated.
	The form constructor accepts a `choices` argument in the form
		{
			'choiceFieldName1': [('option1', 'Option 1'), ('option2', 'Option 2'), ...],
			'choiceFieldName1': [...]
		}
	These options are appended to any choices that may already be defined for the fields.
	'''

	def __init__(self, *args, **kwargs):
		try:
			fieldChoices = kwargs.pop('choices')
		except KeyError:
			fieldChoices = {}

		super(FormWithDynamicChoices, self).__init__(*args, **kwargs)
		for fieldName, choices in fieldChoices.items():
			if fieldName in self.fields:
				self.fields[fieldName].choices += choices
