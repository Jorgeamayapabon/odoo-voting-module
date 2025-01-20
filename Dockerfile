FROM odoo:18.0

COPY odoo.conf /etc/odoo/

WORKDIR /mnt/extra-addons

COPY custom_addons /mnt/extra-addons
