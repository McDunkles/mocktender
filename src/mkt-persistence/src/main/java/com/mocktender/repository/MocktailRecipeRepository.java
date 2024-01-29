package com.mocktender.repository;

import com.mocktender.model.MocktailRecipe;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RestResource;

import java.util.List;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * JPA Repository responsible for making queries to the database that deal with the 'mocktail_recipe' table
 * and returns the filtered results
 */
public interface MocktailRecipeRepository extends JpaRepository<MocktailRecipe, String> {

    @RestResource(path="findByName", rel="findByName", exported = false)
    List<MocktailRecipe> findByName(@Param("name") String name);

    @Override
    @RestResource(exported = false)
    List<MocktailRecipe> findAll();

}
