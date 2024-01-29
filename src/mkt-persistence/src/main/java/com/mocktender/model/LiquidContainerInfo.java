package com.mocktender.model;

import javax.persistence.*;

import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

import lombok.Getter;
import lombok.Setter;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Represents the 'LiquidContainerInfo' table in the database
 */
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "LiquidContainerInfo")
@Entity
public class LiquidContainerInfo {

    @Id //Primary key
    @Column(name = "containerNo", nullable = false)
    private int containerNo;

    @Column(name = "liquid", nullable = false)
    private String liquid;

    @Column(name = "liquidCapacity", nullable = false)
    private int liquidCapacity;

    @Column(name = "liquidLevelPercentage", nullable = false)
    private int liquidLevelPercentage;


    public String toString() {
        return "ID = "+containerNo+"; Liquid = "+liquid;
    }

}
