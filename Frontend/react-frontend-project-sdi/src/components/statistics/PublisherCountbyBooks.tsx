import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
} from "@mui/material";
import React from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Book } from "../../models/book";
import { Publisher } from "../../models/publisher";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import { BACKEND_API_URL } from "../../constants";
import { PublisherNrBooksDTO } from "../../models/PublisherNrBooksDTO";


export const PublisherCountbyBooksShowAll = () => {
    const [loading, setLoading] = useState(false);
	const [publisherBooks, setPublisherBooks] = useState<PublisherNrBooksDTO[]>([]);
	useEffect( () => {
		setLoading(true);
		fetch(`${BACKEND_API_URL}/Publisher/PublisherCountbyBooks/`)
		.then((response) => response.json())
		.then((data) => {
			setPublisherBooks(data);
			setLoading(false);
		});
	}, []);

	return (
		<Container>
			<h1>Statistic - Total number of books of the publishers</h1>
			{loading && <CircularProgress/>}
			{!loading && publisherBooks.length == 0 && <p>No data.</p>}
			{!loading && publisherBooks.length > 0 && (
				<TableContainer component={Paper}>
					<Table sx={{minWidth: 650}} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell align="center">#</TableCell>
								<TableCell align="center">Publisher ID</TableCell>
								<TableCell align="center">Publisher Name</TableCell>
								<TableCell align="center">Number of books</TableCell>
							</TableRow>
						</TableHead>
						<TableBody>
							
							{publisherBooks.map((publisherBooks: PublisherNrBooksDTO, index) => (
								<TableRow key={(publisherBooks.id as Publisher).id}>
									<TableCell  align="center" component="th" scope = "row">{index+1}</TableCell>
									<TableCell  align="center" component="th" scope = "row"><>{publisherBooks.id}</></TableCell>
									<TableCell  align="center" component="th" scope = "row">{publisherBooks.name}</TableCell>
									<TableCell  align="center" component="th" scope = "row">{publisherBooks.nrBooksPublished}</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			)}
		</Container>
	)

}