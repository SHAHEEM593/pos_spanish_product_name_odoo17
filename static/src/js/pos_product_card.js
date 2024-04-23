/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";

patch(ProductCard.prototype, {
productsToDisplay(){
            return {
            ...super.productsToDisplay(),
            spanish_name: this.get_product().spanish_name,
        };
  }
});

