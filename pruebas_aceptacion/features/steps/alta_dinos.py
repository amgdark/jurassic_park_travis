from behave import given, when, then


@given(u'Que ingreso al formulario para llenar los datos del dinosaurios')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Que ingreso al formulario para llenar los datos del dinosaurios')


@given(u'escribo los datos: nombre "t-rex", altura: "5", periodo: "cretacio"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given escribo los datos: nombre "t-rex", altura: "5", periodo: "cretacio"')


@when(u'presiono el botón agregar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When presiono el botón agregar')


@then(u'puedo ver el dinosario "t-rex" en la lista de dinosaurios')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then puedo ver el dinosario "t-rex" en la lista de dinosaurios')