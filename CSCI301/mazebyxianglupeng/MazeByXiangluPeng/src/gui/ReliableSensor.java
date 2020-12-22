package gui;

import generation.CardinalDirection;
import generation.Maze;
import gui.Robot.Direction;

/**
* Responsibility: The ReliableSensor provides information how for it is
* to a wall for a given position and in a specific direction.
* @author Xianglu Peng
*
*/

public class ReliableSensor implements DistanceSensor {
	
	private Controller controller;
	private Maze maze;
	public CardinalDirection cd;
	
	
	
	/**
	 * Tells the distance to an obstacle (a wallboard) that the sensor
	 * measures.
	 */
	@Override
	public int distanceToObstacle(int[] currentPosition, CardinalDirection currentDirection, float[] powersupply)
			throws Exception {
		
		int distance = 0; //count the distance 
		
		// if the robot does not have sensor at the given direction, throw exception
		// get the relative direction of the robot

		int x = currentPosition[0];
		int y = currentPosition[1];
			
		
		while (!controller.getMazeConfiguration().hasWall(x, y, currentDirection)) {
			distance ++;

			if (currentDirection == CardinalDirection.East || currentDirection == CardinalDirection.West) {
				x = x + currentDirection.getDirection()[0];
			}else {
				y = y + currentDirection.getDirection()[1];
			}
			
			if (x < 0 || x > controller.getMazeConfiguration().getWidth() - 1 || y < 0 || y > controller.getMazeConfiguration().getHeight() - 1) {
	
				return Integer.MAX_VALUE;
			}
			
		}
		
						
		return distance;
		
	}

	/**
	 * Provides the maze information that is necessary to make
	 * a DistanceSensor able to calculate distances.
	 * @param maze the maze for this game
	 */
	@Override
	public void setController(Controller c) {
		this.controller = c;
		
	}
	
	@Override
	public void setMaze(Maze maze) {
		this.maze = maze;
	}

	
	/**
	 * Provides the angle, the relative direction at which this 
	 * sensor is mounted on the robot.
	 * If the direction is left, then the sensor is pointing
	 * towards the left hand side of the robot at a 90 degree
	 * angle from the forward direction. 
	 * @param mountedDirection is the sensor's relative direction
	 * @throws IllegalArgumentException if parameter is null
	 */
	@Override
	public void setSensorDirection(Direction mountedDirection) {
		switch(mountedDirection) {
		
		case LEFT:
			cd = controller.getCurrentDirection().oppositeDirection().rotateClockwise();
			break;
			
		case BACKWARD:
			cd = controller.getCurrentDirection().oppositeDirection();
			break;
			
		case FORWARD:
			cd = controller.getCurrentDirection();
			break;
			
		case RIGHT:
			cd = controller.getCurrentDirection().rotateClockwise();
			break;
			
		default:
			break;
		}
		
	}

	
	/**
	 * Returns the amount of energy this sensor uses for 
	 * calculating the distance to an obstacle exactly once.
	 * This amount is a fixed constant for a sensor.
	 * @return the amount of energy used for using the sensor once
	 */
	@Override
	public float getEnergyConsumptionForSensing() {
		// TODO Auto-generated method stub
		return 1;
	}

	@Override
	public void startFailureAndRepairProcess(int meanTimeBetweenFailures, int meanTimeToRepair)
			throws UnsupportedOperationException {
		// TODO Auto-generated method stub
		throw new UnsupportedOperationException("Method not supported.");
		
	}

	@Override
	public void stopFailureAndRepairProcess() throws UnsupportedOperationException {
		// TODO Auto-generated method stub
		throw new UnsupportedOperationException("Method not supported.");
		
	}

}
