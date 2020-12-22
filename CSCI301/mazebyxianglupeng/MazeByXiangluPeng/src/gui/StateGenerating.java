package gui;

import generation.Factory;
import generation.Floorplan;
import generation.Maze;
import generation.MazeFactory;
import generation.Order;
import gui.Constants.UserInput;

/**
 * Class handles the user interaction
 * while the game is in the second stage
 * where the user sees a progress bar while a maze
 * is generated by the factory.
 * This class is part of a state pattern for the
 * Controller class. It is a ConcreteState.
 * 
 * It implements a state-dependent behavior
 * that controls the display and reacts to key board input from a user. 
 * At this point user keyboard input is first dealt with a key listener (SimpleKeyListener)
 * and then handed over to a Controller object by way of the keyDown method.
 * 
 * Responsibilities:
 * Show the generating screen and the progress during generation,
 * Accept input interrupt maze generation and return to title screen,  
 * Generate a maze with the maze factory.
 *
 * This code is refactored code from Maze.java by 
 * Paul Falstad, www.falstad.com, Copyright (C) 1998, all rights reserved
 * Paul Falstad granted permission to modify and use code for teaching purposes.
 * Refactored by Peter Kemper
 */
public class StateGenerating extends DefaultState implements Order {
    SimpleScreens view;
    MazePanel panel;
    Controller control;
    // Filename if maze is loaded from file, can be null
    private String filename;
    
    // about the maze and its generation
    private int seed; // the seed value used for the random number generator
    private int skillLevel; // user selected skill level, i.e. size of maze
    private Builder builder; // selected maze generation algorithm
    private boolean perfect; // selected type of maze, i.e. 
    // perfect == true: no loops, i.e. no rooms
    // perfect == false: maze can support rooms
   
    // The factory is used to calculate a new maze configuration
    // The maze is computed in a separate thread which makes 
    // communication with the factory slightly more complicated.
    // Check the factory interface for details.
    protected Factory factory;
    // The maze configuration produced by the factory
    //private MazeConfiguration mazeConfig; 

    private int percentdone;        // describes progress during generation phase

    boolean started;
    
    /**
     * Constructor uses default settings such that a Depth-First-Search algorithm 
     * is used as the generation method a maze of smallest possible size.
     */
    public StateGenerating() {
        filename = null;
        factory = new MazeFactory() ;
        skillLevel = 0; // default size for maze
        builder = Order.Builder.DFS; // default algorithm
        perfect = false; // default: maze can have rooms
        percentdone = 0;
        started = false;
        seed = 13; // default: an arbitrary fixed value
    }
    
    //////// trivial set methods from State interface ////////////////////////
    // override default implementation
    @Override
    public void setFileName(String filename) {
        this.filename = filename;  
    }
    @Override
    public void setSkillLevel(int skillLevel) {
        this.skillLevel = skillLevel;
    }
    @Override
    public void setBuilder(Builder builder) {
        this.builder = builder;
    }
    @Override
    public void setPerfect(boolean isPerfect) {
        perfect = isPerfect;
    }
    @Override
	public void setSeed(int seed) {
        this.seed = seed;  
    }
    /**
     * Loads maze from file and returns a corresponding maze configuration.
     * @param filename, not null
     */
    private Maze loadMazeConfigurationFromFile(String filename) {
        // load maze from file
        MazeFileReader mfr = new MazeFileReader(panel, filename) ;
        // obtain MazeConfiguration
        return mfr.getMazeConfiguration();
    }
    /**
     * Start the maze generation.
     * @param controller needed to be able to switch states, not null
     * @param panel is the UI entity to produce the generating screen on 
     */
    public void start(Controller controller, MazePanel panel) {
        started = true;
        // keep the reference to the controller to be able to call method to switch the state
        control = controller;
        // keep the reference to the panel for drawing
        this.panel = panel;
        // init mazeview, controller is needed for generating screen to update progress bar
        view = new SimpleScreens();
        // reset percentage for progress
        percentdone = 0;
        // if given a filename, load maze from file
        // otherwise, show view and order maze from factory
        if (filename != null) {
            // load maze from file
            // push results into controller, imitating maze factory delivery
            deliver(loadMazeConfigurationFromFile(filename));
            // reset filename, next round will be generated again
            filename = null;  
        } else {
            // common case: generate maze with some algorithm
            assert null != factory : "Controller.init: factory must be present";
            // draw the initial screen
            draw();
            // make maze factory produce a maze 
            // operates with background thread
            // method returns immediately, 
            // maze will be delivered later by calling this.deliver method
            // this object implements Order, so it carries the spec for the maze
            // to be generated
            factory.order(this) ;
        }
    }
    
    /**
     * Method incorporates all reactions to keyboard input in original code, 
     * The simple key listener calls this method to communicate input.
     * Method requires {@link #start(Controller, MazePanel) start} to be
     * called before.
     * @param key provides the feature the user selected
     * @param value is not used, exists only for consistency across State classes
     */
    public boolean keyDown(UserInput key, int value) {
        if (!started)
            return false;

        // user could interrupt generation by pressing esc
        if (key == UserInput.ReturnToTitle) {
            factory.cancel();
            control.switchToTitle();
        }
        else {
            System.out.println("StateTitle:unexpected command:" + key);
        }    
        return true;
    }
    /**
     * The deliver method is the call back method for the background
     * thread operated in the maze factory to deliver the ordered
     * product, here the generated maze in its container, 
     * the MazeConfiguration object.
     */
    @Override
    public void deliver(Maze mazeConfig) {
        // WARNING: DO NOT REMOVE, USED FOR GRADING PROJECT ASSIGNMENT
        if (Floorplan.deepdebugWall)
        {   // for debugging: dump the sequence of all deleted walls to a log file
            // This reveals how the maze was generated
            mazeConfig.getFloorplan().saveLogFile(Floorplan.deepedebugWallFileName);
        }
        control.switchFromGeneratingToPlaying(mazeConfig);
    }
    //////////// set of trivial get methods ////////////////////////
    @Override
    public int getSkillLevel() {
        return skillLevel;
    }
    @Override
    public Builder getBuilder() {
        return builder;
    }
    @Override
    public boolean isPerfect() {
        return perfect;
    }
    @Override
    public int getSeed() {
    	return seed;
    }
    public int getPercentDone() {
        return percentdone;
    }
    /**
     * Allows external increase to percentage in generating mode.
     * Internal value is only updated if it exceeds the last value and is less or equal 100
     * @param percentage gives the new percentage on a range [0,100]
     * @return true if percentage was updated, false otherwise
     */
    @Override
    public void updateProgress(int percentage) {
        if (this.percentdone < percentage && percentage <= 100) {
            this.percentdone = percentage;
            draw() ;
        }
    }
    /**
     * Draws the current state of maze generation on the screen
     */
    private void draw() {
    	// draw the content on the panel
    	view.redrawGenerating(panel, getPercentDone());
        // update the screen with the buffer graphics
        panel.commit() ;
    }
}



