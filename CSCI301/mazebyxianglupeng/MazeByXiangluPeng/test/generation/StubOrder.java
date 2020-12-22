package generation;

public class StubOrder implements Order{
	
	private Builder builder;
	private Maze mazeConfig;
	private int skillLevel;
	private boolean perfect;
	
	
	public StubOrder(Builder builder, int skillLevel, boolean perfect) {
		this.builder = builder;
		this.mazeConfig = new MazeContainer();
		this.skillLevel = skillLevel;
		this.perfect = perfect;
		
		
	}
	
	public Builder getBuilder() {
		
		return builder;
	}
	
	public int getSkillLevel() {
		
		return skillLevel;
	}
	

	public boolean isPerfect() {
		
		return perfect;
	}
	
	public void deliver(Maze mazeConfig) {
		
		this.mazeConfig = mazeConfig;
	}

	
	public Maze getMaze() {
		
		return mazeConfig;
	}
	@Override
	public void updateProgress(int percentage) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public int getSeed() {
		// TODO Auto-generated method stub
		return 0;
	}
	
	
}