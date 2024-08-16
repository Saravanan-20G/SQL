select * from products

CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    Title VARCHAR(100),
    Genre VARCHAR(50),
    ReleaseYear INT,
    Director VARCHAR(50)
);
CREATE TABLE Ratings (
    RatingID INT PRIMARY KEY,
    MovieID INT,
    Rating INT,
    ReviewDate DATE,
    ReviewerName VARCHAR(50),
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
);

INSERT INTO Movies (MovieID, Title, Genre, ReleaseYear, Director)
VALUES
(1, 'Inception', 'Sci-Fi', 2010, 'Christopher Nolan'),
(2, 'The Dark Knight', 'Action', 2008, 'Christopher Nolan'),
(3, 'Interstellar', 'Sci-Fi', 2014, 'Christopher Nolan'),
(4, 'The Matrix', 'Sci-Fi', 1999, 'Lana Wachowski, Lilly Wachowski'),
(5, 'Pulp Fiction', 'Crime', 1994, 'Quentin Tarantino'),
(6, 'The Shawshank Redemption', 'Drama', 1994, 'Frank Darabont'),
(7, 'The Godfather', 'Crime', 1972, 'Francis Ford Coppola'),
(8, 'The Godfather Part II', 'Crime', 1974, 'Francis Ford Coppola'),
(9, 'Fight Club', 'Drama', 1999, 'David Fincher'),
(10, 'Forrest Gump', 'Drama', 1994, 'Robert Zemeckis');


INSERT INTO Ratings (RatingID, MovieID, Rating, ReviewDate, ReviewerName)
VALUES
(1, 1, 9, '2024-08-01', 'John Doe'),
(2, 2, 10, '2024-08-02', 'Jane Smith'),
(3, 3, 8, '2024-08-03', 'Alice Johnson'),
(4, 4, 9, '2024-08-04', 'Bob Brown'),
(5, 5, 9, '2024-08-05', 'Charlie Davis'),
(6, 6, 10, '2024-08-06', 'David Evans'),
(7, 7, 10, '2024-08-07', 'Ella Wilson'),
(8, 8, 9, '2024-08-08', 'Frank Harris'),
(9, 9, 8, '2024-08-09', 'Grace Lee'),
(10, 10, 9, '2024-08-10', 'Hannah Martin'),
(11, 1, 8, '2024-08-11', 'Ivy Scott'),
(12, 3, 9, '2024-08-12', 'Jack White'),
(13, 4, 10, '2024-08-13', 'Kathy Young'),
(14, 5, 7, '2024-08-14', 'Leo Walker'),
(15, 6, 9, '2024-08-15', 'Mia King');

select *  from movies where genre='Sci-Fi'
select * from movies where releaseyear > 1990

select * from ratings

create table movierating as
select * from ratings
inner join movies on movies.movieid=ratings.movieid

CREATE TABLE MovieRating AS
SELECT * 
FROM Ratings
INNER JOIN Movies 
ON Movies.MovieID = Ratings.MovieID;


CREATE TABLE MovieRating AS

SELECT 
    Ratings.RatingID,
    Ratings.MovieID AS RatingMovieID,  -- Alias the MovieID from Ratings
    Ratings.Rating,
    Ratings.ReviewDate,
    Ratings.ReviewerName,
    Movies.MovieID,  -- Select the MovieID from Movies
    Movies.Title,
    Movies.Genre,
    Movies.ReleaseYear,
    Movies.Director
FROM 
    Ratings
INNER JOIN 
    Movies 
ON 
    Movies.MovieID = Ratings.MovieID;

select * from MovieRating

select * from movierating avg(rating) as avgrating

SELECT 
    MovieID,
    RatingID,
    Rating,
    ReviewDate,
    ReviewerName,
    Title,
    Genre,
    ReleaseYear,
    Director,
    AVG(Rating) OVER() AS AvgRating  -- Calculate the average rating
FROM 
    MovieRating;
select title,genre,avg(rating) as avgrating from movierating
SELECT 
    MovieID,
    Title,
    Genre,
    ReleaseYear,
    Director,
    AVG(Rating) AS AvgRating
FROM 
    MovieRating
	
SELECT 
    MovieID,
    Title,
    Genre,
    ReleaseYear,
    Director,
    AVG(Rating) AS AvgRating
FROM 
    MovieRating
GROUP BY 
    MovieID, Title, Genre, ReleaseYear, Director;

select title,genre,releaseyear,avg(rating) as avgrating from movierating;

SELECT 
    Title,
    Genre,
    ReleaseYear,
    Rating,
    AVG(Rating) OVER() AS AvgRating  
FROM MovieRating;

select title,genre,AVG(rating) over() as avgrating from movierating