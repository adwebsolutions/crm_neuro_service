{
    'name': 'Neuro Service CRM campos adicionales',
    'category': 'Tools',
    'summary': 'Incluir campos adicionales en el crm',
    'website': 'https://www.adweb.mx',
    'version': '1.0',
    'description': """
Modulo de ADWEB para Neuro Service - CRM
===================================
    Este módulo incluye un grupo de campos nuevos a los modelos res.parters y crm.lead, para cumplir los requerimientos de Neuro Service

    
        """,
    'author': 'ADWEB',
    'depends': ['crm'], 
    'external_dependencies': {},
    'data': ['views/crm_custom_fields.xml','views/partner_custom_fields.xml'],
    'installable': True,
    'auto_install':False,
    'active':False,
}
