package gui;

import gui.Constants.UserInput;

/**
 * 
 * @author Xianglu Peng
 *
 */
public class StateLosing extends DefaultState {
	SimpleScreens view;
    MazePanel panel;
    Controller control;
    
    
    boolean started;
    int pathLength;
    float energyConsumption;
    
    public StateLosing() {
        pathLength = 0;
        started = false;
    }
    
    /**
     * Start the game by showing the final screen with a winning message.
     * @param controller needed to be able to switch states, must be not null
     * @param panel is the UI entity to produce the screen on 
     */
    public void start(Controller controller, MazePanel panel) {
        started = true;
        // keep the reference to the controller to be able to call method to switch the state
        control = controller;
        // keep the reference to the panel for drawing
        this.panel = panel;
        // init mazeview, controller not needed for final screen
        view = new SimpleScreens();

        if (panel == null) {
    		System.out.println("StateLosing.start: warning: no panel, dry-run game without graphics!");
    		return;
    	}
        // otherwise show finish screen with winning message
        // draw content on panel
        view.redrawFinish(panel,false,pathLength,energyConsumption);
        // update screen with panel content
        panel.commit();

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
//    	System.out.println("From StateLosing: keyDown");
        if (!started)
            return false;
        // for any keyboard input switch to title screen
        control.switchToTitle();    
        return true;
    }

    @Override
    public void setPathLength(int pathLength) {
        this.pathLength = pathLength;
    }
    
    public void setEnergyComsumtion(float energy) {
        this.energyConsumption = energy;
    }
}


