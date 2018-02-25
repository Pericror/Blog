<?php
/*
@company: Pericror
Description:
    Demo code for https://www.pericror.com/software/dynamically-update-wordpress-page-facebook-open-graph-tags/
*/

add_action( 'wpseo_opengraph', 'change_yoast_seo_og_meta' );

function change_yoast_seo_og_meta() {
    /* Check if the post ID matches the post we want to update open graph tags for. */
    if ( is_single ( 12345 ) ) {
        /* Add filters for existing yoast open graph tags. */
        add_filter('wpseo_opengraph_desc', 'custom_opengraph_desc', 10, 1);
        add_filter('wpseo_opengraph_title', 'custom_opengraph_title');
        add_filter('wpseo_opengraph_image', 'custom_opengraph_image', 10, 2);
    }
}

function custom_opengraph_desc( $desc ) {
    return "Updated open graph description!";
}

function custom_opengraph_title( $title ) {
    return "Updated open graph title!";
}

function custom_opengraph_image( $image ) {
    return "www.pericror.com/images/updatedImage.png";
}