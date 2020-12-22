package generation;

import static org.junit.Assert.*;
import org.junit.jupiter.api.Test;
import generation.Order.Builder;

public class MazeFactoryTest{
	

	private MazeFactory factory;
	private StubOrder stub;
	private MazeFactory factoryDFS;
	private StubOrder stubDFS;
	private MazeFactory factoryPrim;
	private StubOrder stubPrim;
	private MazeFactory factoryEller;
	private StubOrder stubEller;
	
	
	/* Pseudocode for MazeFatoryTest
	 * 
	 * Tests for mazes generated all of the three methods 
	 * 
	 * 1. testOneExit
	 * 
	 * - Method under test: stub.getMaze.isExitPosition(x,y)
	 * 
	 * - Use for loops to go over each cell, use stub.getMaze.isExitPosition(x,y) to find exit, count the number of exits found
	 * 
	 * - Correct behavior:: To check if there's only one exit.
	 * 
	 * 
	 * 
	 * 2. testExitisReachable
	 * 
	 * - Method under test: stub.getMaze().getDistanceToExit(x, y)
	 * 
	 * - Use for loops to go over each cell, use stub.getMaze().getDistanceToExit(x, y) to 
	 *   check if there exist cells that have distance to exit that equal infinity
	 * 
	 * - Correct behavior:: If there's no cell has distance to exit that equals infinity, then the exit is reachable.
	 * 
	 * 
	 * 
	 * 3. testMaximumDistancetoExit
	 * 
	 * - Method under test: stub.getMaze.getDistanceToExit(x,y),stub.getMaze().getStartingPosition();
	 * 
	 * - Use for loops to go over each cell, use stub.getMaze.getDistanceToExit(x,y) to find the cell that has the
	 *   maximum distance to the exit, compare the x-y coordinate with the starting point
	 *  
	 * - Correct behavior: The indices of the point that has maximum distance match the x-y values of the starting point.
	 * 
	 * 
	 */
	
	
	
	public void setup() {
		factoryDFS = new MazeFactory();
		stubDFS = new StubOrder(Builder.DFS, 1, true);
		factoryPrim = new MazeFactory();
		stubPrim = new StubOrder(Builder.Prim, 1, true);
		factoryEller = new MazeFactory();
		stubEller = new StubOrder(Builder.Eller, 1, true);
		factory = new MazeFactory();
		stub = new StubOrder(Builder.DFS, 1, true);
		assertNotNull(factory);
		assertNotNull(stub);
	}
	 

	@Test
	public void testwaitTillDelivered_DFS() {
		setup();
		assertTrue(factoryPrim.order(stubDFS));
	}
	
	
	@Test

	public void testwaitTillDelivered_Prim() {
		setup();
		assertTrue(factoryPrim.order(stubPrim));
	}
	
	@Test
	public void testwaitTillDelivered_Eller() {
		setup();
		assertTrue(factoryEller.order(stubEller));
	}
	
	
	/**
	 * Test case: Check if the generated maze has only one exit
	 * <p>
	 * Method under test: Prim, stub.getMaze.isExitPosition(x,y)
	 * <p>
	 * Correct behavior: There's only one exit for this maze.
	 */
	@Test
	public void testOneExit_Prim() {
		setup();
		factoryPrim.order(stubPrim);
		factoryPrim.waitTillDelivered();
		
		int c = 0;
		for(int x = 0; x < stubPrim.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubPrim.getMaze().getHeight(); y++) {
				if(stubPrim.getMaze().getFloorplan().isExitPosition(x,y) == true) {
						c++;
					
				}
			}
		}
		
		assertEquals(1,c);
	}
	
	/**
	 * Test case: Check if the generated maze has only one exit
	 * <p>
	 * Method under test: DFS, stub.getMaze.isExitPosition(x,y)
	 * <p>
	 * Correct behavior: There's only one exit for this maze.
	 */
	@Test
	public void testOneExit_DFS() {
		setup();
		factoryDFS.order(stubDFS);
		factoryDFS.waitTillDelivered();
		
		int c = 0;
		for(int x = 0; x < stubDFS.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubDFS.getMaze().getHeight(); y++) {
				if(stubDFS.getMaze().getFloorplan().isExitPosition(x,y) == true) {
						c++;
					
				}
			}
		}
		assertEquals(1,c);
	}
	
	
	/**
	 * Test case: Check if the generated maze has only one exit
	 * <p>
	 * Method under test: Eller, stub.getMaze.isExitPosition(x,y)
	 * <p>
	 * Correct behavior: There's only one exit for this maze.
	 */
	@Test
	public void testOneExit_Eller() {
		setup();
		factoryEller.order(stubEller);
		factoryEller.waitTillDelivered();
		
		int c = 0;
		for(int x = 0; x < stubEller.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubEller.getMaze().getHeight(); y++) {
				if(stubEller.getMaze().getFloorplan().isExitPosition(x,y) == true) {
						c++;
					
				}
			}
		}
		assertEquals(1,c);
	}
	
	/**
	 * Test case: Check if the exit is reachable
	 * <p>
	 * Method under test: DFS, stubDFS.getMaze().getDistanceToExit(x, y)
	 * <p>
	 * Correct behavior: There's no cell that has distance to exit equals infinity.
	 */
	@Test
	public void testExitisReachable_DFS() {
		setup();
		factoryDFS.order(stubDFS);
		factoryDFS.waitTillDelivered();
		
		
		int c = 0;
		for(int x = 0; x < stubDFS.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubDFS.getMaze().getHeight(); y++) {
				if(stubDFS.getMaze().getDistanceToExit(x, y) == generation.Distance.INFINITY) {
						c++;
				}
			}
		}
		assertEquals(0,c);
	}
	
	
	/**
	 * Test case: Check if the exit is reachable.
	 * <p>
	 * Method under test: Prim, stubPrim.getMaze().getDistanceToExit(x, y)
	 * <p>
	 * Correct behavior: There's no cell that has distance to exit equals infinity.
	 */
	@Test
	public void testExitisReachable_Prim() {
		setup();
		factoryPrim.order(stubPrim);
		factoryPrim.waitTillDelivered();
		
		int c = 0;
		for(int x = 0; x < stubPrim.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubPrim.getMaze().getHeight(); y++) {
				if(stubPrim.getMaze().getDistanceToExit(x, y) == generation.Distance.INFINITY) {
						c++;

				}
			}
		}
		assertEquals(0,c);
	}
	
	
	/**
	 * Test case: Check if the exit is reachable
	 * <p>
	 * Method under test: Eller, stubEller.getMaze().getDistanceToExit(x, y)
	 * <p>
	 * Correct behavior: There's no cell that has distance to exit equals infinity.
	 */
	@Test
	public void testExitisReachable_Eller() {
		setup();
		factoryEller.order(stubEller);
		factoryEller.waitTillDelivered();
		
		int c = 0;
		for(int x = 0; x < stubEller.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubEller.getMaze().getHeight(); y++) {
				if(stubEller.getMaze().getDistanceToExit(x, y) == generation.Distance.INFINITY) {
						c++;

				}
			}
		}
		assertEquals(0,c);
	}
	
	
	/**
	 * Test case: Check if the starting point is the point that has maximum 
	 * distance to the exit.
	 * <p>
	 * Method under test: DFS, stubDFS.getMaze.getDistanceToExit(x,y),
	 * stubDFS.getMaze().getStartingPosition();
	 * <p>
	 * Correct behavior: The indices of the point that has maximum distance
	 * match the x, y values of the starting point.
	 */
	
	@Test
	public void testMaximumDistancetoExit_DFS() {
		setup();
		factoryDFS.order(stubDFS);
		factoryDFS.waitTillDelivered();
		int d;
		int temp_x = 0;
		int temp_y = 0;
		d = 0;
		for(int x = 0; x < stubDFS.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubDFS.getMaze().getHeight(); y++) {
				if(stubDFS.getMaze().getDistanceToExit(x, y) > d) {
					d = stubDFS.getMaze().getDistanceToExit(x, y);
					temp_x = x;
					temp_y = y;
					
					
				}
			}
		}
		
		int[] array = stubDFS.getMaze().getStartingPosition();
		assertEquals(temp_x, array[0]);
		assertEquals(temp_y, array[1]);
		
		
	}
	
	/**
	 * Test case: Check if the starting point is the point that has maximum 
	 * distance to the exit.
	 * <p>
	 * Method under test: Prim, stubPrim.getMaze.getDistanceToExit(x,y),
	 * stubPrim.getMaze().getStartingPosition();
	 * <p>
	 * Correct behavior: The indices of the point that has maximum distance
	 * match the x, y values of the starting point.
	 */
	@Test
	public void testMaximumDistancetoExit_Prim() {
		setup();
		factoryPrim.order(stubPrim);
		factoryPrim.waitTillDelivered();
		int d;
		int temp_x = 0;
		int temp_y = 0;
		d = 0;
		for(int x = 0; x < stubPrim.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubPrim.getMaze().getHeight(); y++) {
				if(stubPrim.getMaze().getDistanceToExit(x, y) > d) {
					d = stubPrim.getMaze().getDistanceToExit(x, y);
					temp_x = x;
					temp_y = y;
					
				}
			}
		}
		
		int[] array = stubPrim.getMaze().getStartingPosition();
		assertEquals(temp_x, array[0]);
		assertEquals(temp_y, array[1]);
		
	}
	
	/**
	 * Test case: Check if the starting point is the point that has maximum 
	 * distance to the exit.
	 * <p>
	 * Method under test: Eller, stubEller.getMaze.getDistanceToExit(x,y),
	 * stub.getMaze().getStartingPosition();
	 * <p>
	 * Correct behavior: The indices of the point that has maximum distance
	 * match the x, y values of the starting point.
	 */
	@Test
	public void testMaximumDistancetoExit_Eller() {
		
		setup();
		factoryEller.order(stubEller);
		factoryEller.waitTillDelivered();
		int d;
		int temp_x = 0;
		int temp_y = 0;
		d = 0;
		for(int x = 0; x < stubEller.getMaze().getWidth(); x++) {
			for(int y = 0; y < stubEller.getMaze().getHeight(); y++) {
				if(stubEller.getMaze().getDistanceToExit(x, y) > d) {
					d = stubEller.getMaze().getDistanceToExit(x, y);
					temp_x = x;
					temp_y = y;
					
					
				}
			}
		}
		
		int[] array = stubEller.getMaze().getStartingPosition();
		assertEquals(temp_x, array[0]);
		assertEquals(temp_y, array[1]);
		
		
	}


	
	
	
}
	