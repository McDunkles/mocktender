package com.mocktender.repository;

import com.mocktender.model.Account;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RestResource;

import java.util.List;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * JPA Repository responsible for making queries to the database that deal with the 'account' table
 * and returns the results represented by Java objects
 */
public interface AccountRepository extends JpaRepository<Account, String> {

    @RestResource(path="findByUsername", rel="findByUsername")
    List<Account> findByUsername(@Param("username") String username);

    @Override
    @RestResource(exported = false)
    List<Account> findAll();

}
