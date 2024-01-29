package com.mocktender.firebase;

import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Holds information about the Firebase structure. These values are stored in the program's application.yaml file
 */
@Component
@Getter
public class FirebaseProperties {

    @Value("${firebase.db_name}")
    private String name;

    @Value("${firebase.root_node}")
    private String dbRootNode;

    @Value("${firebase.liquid_level1}")
    private String liquidLevel1;

    @Value("${firebase.liquid_level2}")
    private String liquidLevel2;

    @Value("${firebase.liquid_level3}")
    private String liquidLevel3;

    @Value("${firebase.recipe}")
    private String recipeNode;

}
