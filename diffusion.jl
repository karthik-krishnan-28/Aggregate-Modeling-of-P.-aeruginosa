""" Lattice
    * We use this struct to keep track of nutrient and cell concentrations. So far, there are two main instances of the lattice class in the simulation. For more information, read about Fick's Second Law.
    * nutrient_lattice is a 2D array that keeps track of the amount of nutrient available in each location
    * cell_density_lattice is a 2D array that keeps track of the density of cells in each location. This is directly mappable to the nutrient lattice.

    Lattice Properties
    * lattice_resolution: the dimensions of the lattice are lattice_resolution x lattice_resolutio
    * matrix: the matrix representing the lattice
    * diffusion_coefficient: proporitionality constant between the flux and the gradient of the concentration. """

mutable struct Lattice
    lattice_resolution_x::Int64
    lattice_resolution_y::Int64
    matrix::Matrix{Float64}
    diffusion_coefficient::Int64
end

function initialize_to_uniform(lattice::Lattice, initial_value)
    lattice.matrix = zeros(Float64, lattice.lattice_resolution_y, lattice.lattice_resolution_x) .+ initial_value
    return lattice
end

function initialize_to_random(lattice::Lattice, total_value)
    # Initialize matrix to zeros
    lattice.matrix = zeros(Float64, lattice.lattice_resolution_y, lattice.lattice_resolution_x)
    remaining_resource = total_value
    
    # Generate random values for each cell
    random_values = rand(lattice.lattice_resolution_y, lattice.lattice_resolution_x)
    
    # Normalize the random values so they sum to 1
    normalized_values = random_values / sum(random_values)
    
    # Scale the normalized values to sum to total_value
    lattice.matrix = normalized_values * total_value
    
    return lattice
end

""" This function performs a forward time-centered space solution of the diffusion equation using the Forward Euler
    technique of approximating partial differential equations. 
"""
function calculate_diffusion(lattice)
    
    y_flux_padded = zeros(Float64,lattice.lattice_resolution_y + 2, lattice.lattice_resolution_x)
    
    y_flux_padded[1,:] = lattice.matrix[2,:] .+ (2*INFLOW_GRADIENT*LATTICE_SPACING/lattice.diffusion_coefficient) 
    y_flux_padded[end,:] = lattice.matrix[end-1,:] .- (2*OUTFLOW_GRADIENT*LATTICE_SPACING/lattice.diffusion_coefficient) .* lattice.matrix[end, :]
    y_flux_padded[2:end-1,:] .= lattice.matrix
    
    y_flux = -lattice.diffusion_coefficient * (y_flux_padded[2:end,:] .- y_flux_padded[1:end-1,:])/LATTICE_SPACING
    
    dR = -((y_flux[2:end,:] .- y_flux[1:end-1,:])/LATTICE_SPACING)
    
    x_flux_padded = zeros(Float64,lattice.lattice_resolution_y, lattice.lattice_resolution_x + 2)
    
    x_flux_padded[:,1] = lattice.matrix[:,2] .+ (2*INFLOW_GRADIENT*LATTICE_SPACING/lattice.diffusion_coefficient) 
    x_flux_padded[:,end] = lattice.matrix[:,end-1] .- (2*OUTFLOW_GRADIENT*LATTICE_SPACING/lattice.diffusion_coefficient) .* lattice.matrix[:, end]
    x_flux_padded[:,2:end-1] .= lattice.matrix
    
    x_flux = -lattice.diffusion_coefficient * (x_flux_padded[:,2:end] .- x_flux_padded[:,1:end-1])/LATTICE_SPACING
    
    dR = dR - ((x_flux[:,2:end] .- x_flux[:,1:end-1])/LATTICE_SPACING)
    
    lattice.matrix .+= dR * RESOURCE_DT
end