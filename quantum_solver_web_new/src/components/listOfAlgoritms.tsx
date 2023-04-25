
// MUI imports
import Stack from '@mui/material/Stack';

// algorithm card
import { AlgorithmCard } from './algorithmCard';




export const ListAlgorithm = ({ listAlgorithm }: any) => {
  return (
    <Stack>
      {listAlgorithm.map((algorithm: any, i:number) => (
        <AlgorithmCard 
          algorithmName={algorithm.name} 
          description={algorithm.description} 
          parameters={algorithm.parameters} 
          key= {i}
          />))}
    </Stack>
  )
}