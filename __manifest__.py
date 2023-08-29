{
    'name': "Clothes Market Backend",
    'version': '1.0',
    'depends': ['base'],
    'author': "Oscar Deladas",
    'category': 'Marketing',
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'description': """
    A module to save clothes
    """,
    # data files always loaded at installation
    'data': ['data/ir.model.access.csv',
             'data/clothes_market.suppliers.csv',
             'data/clothes_market.types.csv'],
    # data files containing optionally loaded demonstration data
    'demo': [],
}
