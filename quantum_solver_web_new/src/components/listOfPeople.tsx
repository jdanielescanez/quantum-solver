// MUI imports
import Stack from '@mui/material/Stack';

// people card
import { PeopleCard } from './peopleCard';
import { Grid } from '@mui/material';

type PeopleCardProps = {
  name: string,
  position: string,
  photo: string,
  socialMedia: {
    linkedin: string,
    twitter: string,
    mail: string,
  },
}


export const ListPeople = ({ listPeople }: any) => {
  return (
    <Stack
      sx={{
        justifyContent: "center",
        alignContent: "center",
        display: "flex",
        marginTop: "1em",
        marginBottom: "1em",
      }}>
      <Grid container spacing={2} direction="row">
        {listPeople.map((people: PeopleCardProps, i: number) => (
          <Grid item xs={12} sm={6} md={4} key={i} sx={{
            justifyContent: "center",
            alignContent: "center",
          }}>
            <PeopleCard
              name={people.name}
              position={people.position}
              photo={people.photo}
              socialMedia={people.socialMedia}
              key={i}
            />
          </Grid>
        ))}
      </Grid>
    </Stack >
  )
}