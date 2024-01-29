package com.mocktender.repository;

import com.mocktender.model.LiquidContainerInfo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RestResource;

import java.util.List;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * JPA Repository responsible for making queries to the database that deal with the 'LiquidContainerInfo' table
 * and returns the filtered results
 */
public interface LiquidContainerInfoRepository extends JpaRepository<LiquidContainerInfo, String> {

    @RestResource(path="findByContainerNo", rel="findByContainerNo")
    List<LiquidContainerInfo> findByContainerNo(@Param("containerNo") int containerNo);

    @Override
    @RestResource(exported = false)
    List<LiquidContainerInfo> findAll();

    @Query(value = "SELECT DISTINCT b.type FROM Building b", nativeQuery = true)
    List<String> findDistinctTypes();

}
