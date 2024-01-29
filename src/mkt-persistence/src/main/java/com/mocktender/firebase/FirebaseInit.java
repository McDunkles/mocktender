package com.mocktender.firebase;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.database.*;
import com.mocktender.controller.LiquidContainerInfoController;
import com.mocktender.model.LiquidContainerInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Author: Duncan MacLeod (101160585)
 *
 * Initializes a connection to Firebase
 */
@Service
public class FirebaseInit {

    private FirebaseApp firebaseApp;

    private FirebaseDatabase firebaseDatabase;

    @Autowired
    private LiquidContainerInfoController liquidLevelInfoController;

    @Autowired
    private FirebaseProperties fp;

    /**
     * Initializes the Firebase connection
     *
     * @PostConstruct annotation means it occurs after Spring Beans have been created and
     * injected via the @Autowired annotation
     */
    @PostConstruct
    public void initializeConnection() {
        try {

            //Get path for the serviceAccountKey file, which contains Firebase configuration info
            Path path = Paths.get("src/main/resources/serviceAccountKey.json");

            FileInputStream serviceAccount =
                    new FileInputStream(path.toFile());

            FirebaseOptions options = FirebaseOptions.builder()
                    .setCredentials(GoogleCredentials.fromStream(serviceAccount))
                    .setDatabaseUrl("https://mocktenderdb-default-rtdb.firebaseio.com")
                    .build();

            firebaseApp = FirebaseApp.initializeApp(options, fp.getName());

            firebaseDatabase = FirebaseDatabase.getInstance(firebaseApp, "https://mocktenderdb-default-rtdb.firebaseio.com");


            ValueEventListener listener = new ValueEventListener() {
                @Override
                public void onDataChange(DataSnapshot dataSnapshot) {

                    DataSnapshot snapshot = dataSnapshot.child(fp.getDbRootNode());

                    String[] liquidLevelRawValues = {
                            snapshot.child(fp.getLiquidLevel1()).getValue().toString(),
                            snapshot.child(fp.getLiquidLevel2()).getValue().toString(),
                            snapshot.child(fp.getLiquidLevel3()).getValue().toString(),
                    };

                    String[] liquidLevelValues = {
                            liquidLevelRawValues[0].substring(liquidLevelRawValues[0].indexOf('=')+1, liquidLevelRawValues[0].length()-1),
                            liquidLevelRawValues[1].substring(liquidLevelRawValues[1].indexOf('=')+1, liquidLevelRawValues[1].length()-1),
                            liquidLevelRawValues[2].substring(liquidLevelRawValues[2].indexOf('=')+1, liquidLevelRawValues[2].length()-1)
                    };


                    for (int i = 0; i<liquidLevelValues.length; i++) {

                        LiquidContainerInfo info = liquidLevelInfoController.findByContainerNo(i+1);

                        double level = Double.parseDouble(liquidLevelValues[i]);

                        double capacity = level/info.getLiquidCapacity()*100;

                        //Update the Liquid Levels when a db change is detected
                        liquidLevelInfoController.updateLiquidLevel(i+1, (int)Math.round(capacity));
                    }

                }

                @Override
                public void onCancelled(DatabaseError databaseError) {
                    System.out.println("Database Error. Error Details:\n"+databaseError.getDetails());
                }
            };

            firebaseDatabase.getReference().addValueEventListener(listener);


        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }

    public FirebaseDatabase getFirebaseDatabase() {return firebaseDatabase;}
}
