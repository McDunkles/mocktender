package com.mocktender;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Starts the Spring Program
 */
@SpringBootApplication
@EntityScan(basePackages = {"com.mocktender.model"})
@ComponentScan(basePackages = {"com.mocktender.cors", "com.mocktender.controller", "com.mocktender.firebase"})
public class MocktenderPersistenceLayerApplication {
	public static void main(String[] args) {SpringApplication.run(MocktenderPersistenceLayerApplication.class, args);}
}
