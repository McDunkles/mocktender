package com.mocktender.firebase;

import com.google.firebase.database.*;
import com.mocktender.model.MocktailRecipe;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Service responsible for sending a Mocktail recipe to Firebase for the machine to make
 */
@Service
public class FirebaseService {

    @Autowired
    private FirebaseInit firebaseInitialize;

    @Autowired
    private FirebaseProperties fp;

    /**
     * Sends a Mocktail recipe to Firebase for the IOController to receive
     * @param recipe - The Mocktail Recipe to send
     */
    public void sendRecipe(MocktailRecipe recipe) {

        FirebaseDatabase firebaseDatabase = firebaseInitialize.getFirebaseDatabase();

        DatabaseReference.CompletionListener completionListener = (databaseError, databaseReference) -> System.out.println("Value Written!");

        DatabaseReference reference = firebaseDatabase.getReference()
                .child(fp.getDbRootNode())
                .child(fp.getRecipeNode());

        float totalLiquid = recipe.getAmount1() + recipe.getAmount2() + recipe.getAmount3();

        double[] liquids = {recipe.getAmount1(), recipe.getAmount2(), recipe.getAmount3()};

        int[] percentages = new int[liquids.length];

        for (int i = 0; i< percentages.length; i++) {
            percentages[i] = (int)Math.round(liquids[i]/totalLiquid * 100.0);
        }


        DatabaseReference percentagesReference = reference.child("drinkPercentages");

        percentagesReference.child("l1").setValue(percentages[0], completionListener);
        percentagesReference.child("l2").setValue(percentages[1], completionListener);
        percentagesReference.child("l3").setValue(percentages[2], completionListener);

        reference.child("drinkSize").setValue(totalLiquid, completionListener);


        reference.child("ack").setValue(false, completionListener);
    }


}
