package com.mocktender.model;

import javax.persistence.*;

import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

import lombok.Getter;
import lombok.Setter;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Represents the 'liquid' table in the database
 */
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "liquid")
@Entity
public class Liquid {
    @Id //Primary key
    @Column(name = "name", nullable = false)
    private String name;
}
