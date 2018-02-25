<?php
/*
@company: Pericror
Description:
    Demo code for https://www.pericror.com/software/dynamically-update-wordpress-pages-facebook-open-graph-tags/
*/

add_action( 'wpseo_opengraph', 'change_yoast_seo_og_meta' );

function change_yoast_seo_og_meta() {
    /* Check if the post ID matches the post we want to update open graph tags for. */
    if ( is_single ( 12345 ) ) {
        
        /* Define the new open graph tag data we will be using. */ 
        global $spirit_animals;
        $spirit_animals = array(    "Owl",
                                    "Lion",
                                    "Fox");

        global $animal_descriptions;
        $animal_descriptions = array(   "The Owl represents your wise qualities, as you are known for your good decisions.",
                                        "The Lion represents your bravery, as you are known for standing up for what is right.",
                                        "The Fox represents your cunning, as you are known for making sly deals.",
        
        global $animal_images;
        $animal_images = array( "https://pericror.com/wp-content/uploads/animals/owl.png",
                                "https://pericror.com/wp-content/uploads/animals/lion.png",
                                "https://pericror.com/wp-content/uploads/animals/fox.png");
    
        global $random_animal;
        $random_animal = rand(0, count($spirit_animals)-1);
        
        /* Add filters for existing yoast open graph tags. */
        add_filter('wpseo_opengraph_desc', 'spirit_animal_opengraph_desc', 10, 1);
        add_filter('wpseo_opengraph_title', 'spirit_animal_opengraph_title');
        add_filter('wpseo_opengraph_image', 'spirit_animal_opengraph_image', 10, 2);
    }
}


function spirit_animal_opengraph_desc( $desc ) {
    return $GLOBALS['animal_descriptions'][$GLOBALS['random_animal']];
}

function spirit_animal_opengraph_title( $title ) {
    $animal = $GLOBALS['spirit_animals'][$GLOBALS['random_animal']];
    return "Your spirit animal is the " . $animal . "!";
}

function spirit_animal_opengraph_image( $image ) {
    return $GLOBALS['animal_images'][$GLOBALS['random_animal']];
}