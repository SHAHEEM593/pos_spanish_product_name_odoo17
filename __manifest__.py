# -*- coding: utf-8 -*-
{
    'name': "Spanish Product Name POS",
    'version': '17.0.1.0.0',
    'depends': ['base','point_of_sale','school_management'],
    'author': "Shaheem",
    'category': 'category',
    'description': """
   Visible Spanish Name on pos
    """,
    'summary': 'Visible Spanish Name on pos',
    # data files always loaded at installation
    'data': [
        'views/product_product_view.xml',
    ],

    'application': True,
    'installable': True,

    'assets': {
       'point_of_sale._assets_pos': [
           'pos_spanish_product_name/static/src/js/pos_order_line.js',
           'pos_spanish_product_name/static/src/js/pos_product_card.js',
            'pos_spanish_product_name/static/xml/pos_product_widget.xml' ,
            'pos_spanish_product_name/static/xml/pos_screen_orderline.xml' ,
            'pos_spanish_product_name/static/xml/pos_screen_product_card.xml' ,
       ],
    },
}
