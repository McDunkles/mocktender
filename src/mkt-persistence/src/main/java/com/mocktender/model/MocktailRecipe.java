package com.mocktender.model;

import javax.persistence.*;

import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

import lombok.Getter;
import lombok.Setter;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Represents the 'mocktail_recipe' table in the database
 */
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "mocktail_recipe")
@Entity
public class MocktailRecipe {

    @Id //Primary key
    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "liquid1")
    private String liquid1;

    @Column(name = "amount1")
    private float amount1;

    @Column(name = "liquid2")
    private String liquid2;

    @Column(name = "amount2")
    private float amount2;

    @Column(name = "liquid3")
    private String liquid3;

    @Column(name = "amount3")
    private float amount3;

    public String toString() {

        return String.format("Mocktail :: {\nName = %s\nliquid1 = %s, amount1 = %f\nliquid2 = %s, amount2 = %f\nliquid3 = %s, amount3 = %f",
                name, liquid1, amount1, liquid2, amount2, liquid3, amount3);
    }

}
