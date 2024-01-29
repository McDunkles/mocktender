package com.mocktender.controller;

import com.mocktender.model.Liquid;
import com.mocktender.model.MocktailRecipe;
import com.mocktender.repository.MocktailRecipeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Contains the API mappings and function calls that manipulate the 'mocktail_recipe' table in the database
 */
@RestController
@RequestMapping("api/recipes")
public class MocktailRecipeController {

    @Autowired
    MocktailRecipeRepository mocktailsRepo;

    @Autowired
    LiquidController liquidController;

    @GetMapping("/findAll")
    public List<MocktailRecipe> findAllSavedMocktails() {
        return mocktailsRepo.findAll();
    }

    @GetMapping("/findByName")
    public MocktailRecipe findByName(@RequestParam("name") String name) {
        return mocktailsRepo.findByName(name).get(0);
    }


    @RequestMapping(value = "/addMocktail", method = {RequestMethod.GET, RequestMethod.POST})
    public MocktailRecipe addMocktailRecipe(
            @RequestParam("name") String name, @RequestParam("liquid1") String liquid1,
            @RequestParam("amount1") float amount1,
            @RequestParam("liquid2") String liquid2,
            @RequestParam("amount2") float amount2,
            @RequestParam("liquid3") String liquid3,
            @RequestParam("amount3") float amount3
    ) {

        MocktailRecipe mocktail = new MocktailRecipe(name, liquid1, amount1,
                liquid2, amount2, liquid3, amount3);

        //Check to make sure liquids are in repository
        //If not, add them
        String[] liquids = {liquid1, liquid2, liquid3};

        for (String liquid : liquids) {
            List<Liquid> result = liquidController.findByName(liquid);

            if (result.size() == 0) {
                System.out.println("[MocktailRecipeController] Adding Liquid "+liquid+"!");
                liquidController.addLiquid(liquid);
            }
        }

        mocktailsRepo.save(mocktail);
        return mocktail;
    }

}
