# Part of Flectra See LICENSE file for full copyright and licensing details.

{
    'name': 'Return Merchandise Authorizationing',
    'version': '1.0',
    'author': 'Flectra',
    'website': 'https://flectrahq.com',
    'description': """
        Return Merchandise Authorizationing is part of the process of a
        consumer returning a product to receive a refund, replacement or repair
         during the product's warranty period.
    """,
    'category': 'Sales',
    'depends': ['sale_management', 'stock', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'sequences/data_rma_order_sequence.xml',
        'views/rma_request_view.xml',
        'views/replacement_reason_view.xml',
        'views/rma_line_view.xml',
        'views/stock_production_lot_view.xml',
        'views/stock_picking_view.xml',
        'views/warranty_expire_line_view.xml',
        'views/sales_team_view.xml',
        'views/menuitems_view.xml',
        'data/mail_message_subtype_data.xml',
        'data/mail_template_data.xml',
    ],

    'demo': [
        'demo/product_demo.xml',
        'demo/stock_demo.xml',
        'demo/sale_order_demo.xml',
    ],
}
