package com.mocktender.repository;

import com.mocktender.model.Liquid;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RestResource;

import java.util.List;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * JPA Repository responsible for making queries to the database that deal with the 'liquid' table
 * and returns the filtered results
 */
public interface LiquidRepository extends JpaRepository<Liquid, String> {

    @RestResource(path="findByName", rel="findByName")
    List<Liquid> findByName(@Param("name") String name);

    @Override
    @RestResource(exported = false)
    List<Liquid> findAll();

}
