package com.mocktender.controller;

import com.mocktender.firebase.FirebaseService;
import com.mocktender.model.MocktailRecipe;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Contains the API mappings that interact with Firebase, which is the mechanism for communicating with the
 * IOController
 */
@RestController
@RequestMapping("api/firebase")
public class FirebaseController {

    @Autowired
    FirebaseService firebaseService;

    @RequestMapping(value = "/sendRecipe", method = {RequestMethod.GET, RequestMethod.POST})
    public MocktailRecipe sendMocktailRecipe(
            @RequestParam("name") String name, @RequestParam("liquid1") String liquid1,
            @RequestParam("amount1") float amount1,
            @RequestParam("liquid2") String liquid2,
            @RequestParam("amount2") float amount2,
            @RequestParam("liquid3") String liquid3,
            @RequestParam("amount3") float amount3
    ) {

        MocktailRecipe mocktail = new MocktailRecipe(name, liquid1, amount1,
                liquid2, amount2, liquid3, amount3);

        firebaseService.sendRecipe(mocktail);

        return mocktail;
    }



}
